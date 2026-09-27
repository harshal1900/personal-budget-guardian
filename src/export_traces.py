import json
from dotenv import load_dotenv
from langsmith import Client

load_dotenv()
client = Client()

project_name = "personal-budget-guardian-agent"  # match whatever you set as LANGSMITH_PROJECT in .env

runs = client.list_runs(
    project_name=project_name,
    is_root=True,
)

def serialize(run):
    if hasattr(run, "model_dump"):
        return run.model_dump()
    return run.dict()

trace_data = [serialize(run) for run in runs]

with open("exported_traces.json", "w") as f:
    json.dump(trace_data, f, indent=2, default=str)

print(f"Exported {len(trace_data)} traces to exported_traces.json")