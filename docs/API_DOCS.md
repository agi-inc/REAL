# REAL Evals API Documentation

This document describes the API functions available for interacting with the REAL Evals platform.
Below is where you will find your API keys: https://www.realevals.xyz/profile
![API Keys Interface](images/api_keys.png)

API keys are used to make submissions to the REAL Evals platform.

There are currently two main APIs:

1. `get_run_id`: Registers a new evaluation run on the REAL Evals platform and returns a unique run ID.
2. `get_run_results`: Retrieves the results of a previously registered evaluation run.


## Functions

### `get_run_id(api_key: str, model_name: str, run_name: str) -> str`

Registers a new evaluation run on the REAL Evals platform and returns a unique run ID.

#### Parameters:
- `api_key` (str): Your REAL Evals API key for authentication
- `model_name` (str): Name of the model being evaluated
- `run_name` (str): A descriptive name for this evaluation run

#### Returns:
- `str`: A unique run ID that can be used for submitting task results

#### Example:
```python
url = (
            "https://www.realevals.xyz/api/runKey?"
            + urllib.parse.urlencode(
                {
                    "api_key": api_key,
                    "model_name": model_name,
                    "run_name": run_name,
                }
            )
        )
```
#### Notes:
- The run ID is required for submitting task results
- Each run should have a unique run name for easy identification
- The API endpoint used is `https://www.realevals.xyz/api/runKey`

### `get_run_results(api_key: str, display_name: str) -> dict`

Retrieves the results of a previously registered evaluation run.

#### Parameters:
- `api_key` (str): Your REAL Evals API key for authentication
- `display_name` (str): The display name of the run to retrieve results for

#### Returns:
- `dict`: A dictionary containing detailed results of the evaluation run, including:
  - `run_id`: Unique identifier for the run
  - `model_id`: Identifier for the model used
  - `success_rate`: Overall success rate as a percentage
  - `total_runs`: Total number of tasks executed
  - `created_at`: Timestamp when the run was created
  - `runs`: List of individual task results containing:
    - `task_id`: Identifier for the task
    - `retrieved_answer`: The answer provided by the model
    - `evals_passed`: Number of evaluation criteria passed
    - `evals_failed`: Number of evaluation criteria failed
    - `points`: Points earned for the task
    - `accuracy`: Accuracy score for the task
    - `completed_at`: Timestamp when the task was completed
    - `final_state`: Final state of the task execution

#### Example:
```python
url = (
            "https://www.realevals.xyz/api/getRunTask?"
            + urllib.parse.urlencode(
                {
                    "api_key": api_key,
                    "display_name": display_name,
                }
            )
        )
```
