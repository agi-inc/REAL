import json
import os
from pathlib import Path

# Load all task JSON files
tasks_dir = Path(__file__).parent / "browsergym" / "webclones" / "tasks"

# Create a flat list of all tasks
all_tasks = []

for file_path in tasks_dir.glob("*.json"):
    # Load JSON and add to list
    with open(file_path, "r") as f:
        task = json.load(f)
        # Add filename to task for reference
        task["_filename"] = file_path.name
        all_tasks.append(task)

# Function to load experimental LLM-generated tasks
def load_experimental_tasks():
    experimental_file = tasks_dir / "experimental" / "llm-generated.json"
    if experimental_file.exists():
        with open(experimental_file, "r") as f:
            tasks = json.load(f)
            # Add filename to tasks for reference
            for task in tasks:
                task["_filename"] = "experimental/llm-generated.json"
            return tasks
    return []

# Load all tasks including experimental ones
experimental_tasks = load_experimental_tasks()
all_including_experimental = all_tasks + experimental_tasks

# Print count for verification
print(f"Regular tasks: {len(all_tasks)}, Experimental tasks: {len(experimental_tasks)}, Combined: {len(all_including_experimental)}")