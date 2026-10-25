# Verification

- Supplied suite with `--run-llm`: **24 passed**, including the live end-to-end test.
- Added regression checks: **3 passed** (malformed actions and path normalization).
- Offline supplied suite: 23 passed, 1 deliberately skipped live test.
- Runtime: Python 3.12, gpt-4.1-mini, actual OpenAI embeddings and chat API.
- Route: direct OpenAI with the owner's account; Helicone logging was not exercised.

The starter placed pytest_addoption in a test module, where pytest does not
register it. conftest.py registers the flag and provides deterministic offline
embeddings. Each test receives a clean in-process Chroma store, preventing
mock embeddings from mixing with live dimensions. The provided memory, tools,
and client files remain unchanged.

The agent accepts SDK-style tool prefixes and strips a leading workspace/ from
file-tool paths. The system prompt documents the file/execution path distinction.

Default DEMO_TASK also passed: 6 model iterations, 5 tool calls. See live-result.json for actual calls and results.
