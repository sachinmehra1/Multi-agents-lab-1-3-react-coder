"""Run the default task and save its observable tool calls and final result."""
import json
from pathlib import Path
from agent import DEMO_TASK, run_agent

result = run_agent(DEMO_TASK)
Path('verification').mkdir(exist_ok=True)
Path('verification/live-result.json').write_text(json.dumps(vars(result), indent=2))
print(result)
raise SystemExit(int(result.stopped_early))
