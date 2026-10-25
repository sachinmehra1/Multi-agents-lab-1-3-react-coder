"""Regression checks for malformed actions and repository-relative file paths."""
from types import SimpleNamespace
from unittest.mock import MagicMock, patch
from agent import parse_llm_response, run_agent


def test_action_input_must_be_object():
    assert 'parse_error' in parse_llm_response('Thought: x\nAction: write_file\nAction Input: []')


def test_missing_action_is_recoverable():
    assert 'parse_error' in parse_llm_response('unstructured response')


def test_normalizes_tool_namespace_and_workspace_prefix():
    responses = [
        'Thought: write\nAction: functions.write_file\nAction Input: {"path":"workspace/demo.py","content":"x=1"}',
        'Thought: done\nFINAL ANSWER: done',
    ]
    completions = [SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=t))]) for t in responses]
    with patch('agent.client') as client, patch('agent.SemanticMemory') as memory, patch('agent.dispatch_tool', return_value='written') as dispatch:
        memory.return_value.count.return_value = 0
        client.chat.completions.create.side_effect = completions
        result = run_agent('write demo.py')
    dispatch.assert_called_once_with('write_file', {'path': 'demo.py', 'content': 'x=1'})
    assert result.iterations == 2 and not result.stopped_early
