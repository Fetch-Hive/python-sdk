"""
Unit tests for the SSE parser (streaming.py).

Covers SSE1-SSE5 in the SDK test matrix.
No network calls — all tests use FakeResponse which implements the same
interface as httpx.Response for streaming purposes.
"""
import pytest

from fetch_hive_sdk.streaming import _parse_line, aiter_sse, iter_sse


# ── FakeResponse ──────────────────────────────────────────────────────────────


class FakeResponse:
    """
    Minimal stand-in for an httpx streaming response.
    Accepts a list of text chunks that `iter_text` / `aiter_text` will yield.
    """

    def __init__(self, chunks: list[str], status_code: int = 200):
        self._chunks = chunks
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            # Mirror the interface httpx raises
            import httpx
            request = httpx.Request("POST", "https://example.com")
            response = httpx.Response(self.status_code, request=request)
            raise httpx.HTTPStatusError(
                f"Client error '{self.status_code}'",
                request=request,
                response=response,
            )

    def iter_text(self):
        yield from self._chunks

    async def aiter_text(self):
        for chunk in self._chunks:
            yield chunk


def make_sse(events: list[dict], done: bool = True) -> str:
    import json
    lines = "".join(f"data: {json.dumps(e)}\n\n" for e in events)
    return lines + ("data: [DONE]\n\n" if done else "")


# ── _parse_line unit tests (helpers for SSE3, SSE4) ──────────────────────────


class TestParseLine:
    def test_parses_valid_data_line(self):
        result = _parse_line('data: {"type":"response","response":"hi"}')
        assert result == {"type": "response", "response": "hi"}

    def test_returns_none_for_comment(self):
        assert _parse_line(": this is a comment") is None

    def test_returns_none_for_blank(self):
        assert _parse_line("") is None

    def test_returns_none_for_done(self):
        assert _parse_line("data: [DONE]") is None

    def test_returns_none_for_malformed_json(self):
        assert _parse_line("data: {not valid json}") is None

    def test_returns_none_for_event_field(self):
        assert _parse_line("event: message") is None


# ── SSE1: clean single-chunk stream ──────────────────────────────────────────


class TestSse1Clean:
    def test_iter_sse_yields_events(self):
        text = make_sse([
            {"type": "response", "response": "Hello"},
            {"type": "response", "response": " world"},
            {"type": "usage", "request_id": "r1", "usage": {"prompt_tokens": {"total_tokens": 10}, "completion_tokens": {"total_tokens": 5}, "total_tokens": 15}, "stop_reason": "completed"},
        ])
        chunks = list(iter_sse(FakeResponse([text])))
        assert len(chunks) == 3
        assert chunks[0]["response"] == "Hello"
        assert chunks[2]["type"] == "usage"

    @pytest.mark.asyncio
    async def test_aiter_sse_yields_events(self):
        text = make_sse([{"type": "response", "response": "Hello"}])
        chunks = []
        async for chunk in aiter_sse(FakeResponse([text])):
            chunks.append(chunk)
        assert len(chunks) == 1
        assert chunks[0]["response"] == "Hello"


# ── SSE2: chunks split mid-line ───────────────────────────────────────────────


class TestSse2ChunkSplit:
    def test_reassembles_event_from_two_chunks(self):
        full = 'data: {"type":"response","response":"Hi"}\n\ndata: [DONE]\n\n'
        part1 = full[:20]
        part2 = full[20:]
        chunks = list(iter_sse(FakeResponse([part1, part2])))
        assert len(chunks) == 1
        assert chunks[0]["response"] == "Hi"

    def test_reassembles_multiple_events_from_fragments(self):
        full = make_sse([
            {"type": "response", "response": "A"},
            {"type": "response", "response": "B"},
        ])
        # Split into 3-character pieces
        pieces = [full[i:i+3] for i in range(0, len(full), 3)]
        chunks = list(iter_sse(FakeResponse(pieces)))
        assert len(chunks) == 2
        assert chunks[0]["response"] == "A"
        assert chunks[1]["response"] == "B"

    @pytest.mark.asyncio
    async def test_async_reassembles_from_chunks(self):
        full = 'data: {"type":"response","response":"Hi"}\n\ndata: [DONE]\n\n'
        part1, part2 = full[:18], full[18:]
        chunks = []
        async for chunk in aiter_sse(FakeResponse([part1, part2])):
            chunks.append(chunk)
        assert len(chunks) == 1
        assert chunks[0]["response"] == "Hi"


# ── SSE3: non-data lines are skipped ─────────────────────────────────────────


class TestSse3SkipNonData:
    def test_skips_comment_lines(self):
        text = ": comment\n" + make_sse([{"type": "response", "response": "ok"}])
        chunks = list(iter_sse(FakeResponse([text])))
        assert len(chunks) == 1

    def test_skips_blank_lines(self):
        text = "\n\n" + make_sse([{"type": "response", "response": "ok"}])
        chunks = list(iter_sse(FakeResponse([text])))
        assert len(chunks) == 1

    def test_skips_event_and_id_fields(self):
        text = "event: message\nid: 1\n" + make_sse([{"type": "response", "response": "ok"}])
        chunks = list(iter_sse(FakeResponse([text])))
        assert len(chunks) == 1


# ── SSE4: malformed JSON is skipped silently ──────────────────────────────────


class TestSse4MalformedJson:
    def test_continues_after_bad_line(self):
        import json
        text = (
            f'data: {json.dumps({"type": "response", "response": "before"})}\n\n'
            "data: {this is not json}\n\n"
            f'data: {json.dumps({"type": "response", "response": "after"})}\n\n'
            "data: [DONE]\n\n"
        )
        chunks = list(iter_sse(FakeResponse([text])))
        assert len(chunks) == 2
        assert chunks[0]["response"] == "before"
        assert chunks[1]["response"] == "after"

    @pytest.mark.asyncio
    async def test_async_continues_after_bad_line(self):
        import json
        text = (
            f'data: {json.dumps({"type": "response", "response": "ok"})}\n\n'
            "data: {bad}\n\n"
            "data: [DONE]\n\n"
        )
        chunks = []
        async for chunk in aiter_sse(FakeResponse([text])):
            chunks.append(chunk)
        assert len(chunks) == 1
        assert chunks[0]["response"] == "ok"


# ── SSE5: stops at [DONE] ─────────────────────────────────────────────────────


class TestSse5Done:
    def test_stops_at_done(self):
        import json
        text = (
            f'data: {json.dumps({"type": "response", "response": "keep"})}\n\n'
            "data: [DONE]\n\n"
            f'data: {json.dumps({"type": "response", "response": "drop"})}\n\n'
        )
        chunks = list(iter_sse(FakeResponse([text])))
        assert len(chunks) == 1
        assert chunks[0]["response"] == "keep"

    def test_completes_without_done(self):
        import json
        text = f'data: {json.dumps({"type": "response", "response": "only"})}\n\n'
        chunks = list(iter_sse(FakeResponse([text])))
        assert len(chunks) == 1

    def test_raises_on_non_2xx(self):
        import httpx
        with pytest.raises(httpx.HTTPStatusError):
            list(iter_sse(FakeResponse([], status_code=401)))

    @pytest.mark.asyncio
    async def test_async_raises_on_non_2xx(self):
        import httpx
        with pytest.raises(httpx.HTTPStatusError):
            async for _ in aiter_sse(FakeResponse([], status_code=403)):
                pass
