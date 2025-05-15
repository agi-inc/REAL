# Example of using Amazon NovaAct to perform a task on a website
from nova_act import NovaAct
from agisdk.REAL.tasks import all_tasks as tasks
import urllib.parse

# let's just run on dashdish-1
tasks = [task for task in tasks if task["id"] == "omnizon-2"]


run_id = "YOUR_RUN_ID_HERE" # creat a run id on realevals.xyz

for task in tasks:
    goal = task["goal"]
    url = task["website"]["url"]
    task_id = task["id"]
    config_url = url + f"/config?run_id={run_id}&task_id={task_id}"
    print(f"Goal: {goal}")
    with NovaAct(starting_page=config_url) as nova:
        nova.go_to_url(url)
        result = nova.act(goal)
        response = result.response if result.response is not None else "No response"
        print(f"Response: {response}")
        encoded_response = urllib.parse.quote(response)
        nova.go_to_url(url + "/submit?retrieved_answer=" + encoded_response)
        print(f"Submitted response to {url + '/submit?retrieved_answer=' + encoded_response}")
        print("go to your profile in realevals.xyz to see the result")
