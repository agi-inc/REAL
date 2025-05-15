# AGI SDK Harness System

## Overview

The `harness.py` file is a core component of the AGI SDK, providing a unified interface for running AI agents on browser-based tasks. It simplifies the process of setting up, running, and evaluating agents on various tasks while providing features like caching, parallel execution, and leaderboard submission.

## Key Components

### `harness` Class

The main class that orchestrates agent execution, environment setup, and result management. It provides a clean API for running both built-in and custom agents on browsergym tasks.

#### Initialization Parameters

- **Model Configuration**
  - `model`: Name of the AI model to use (e.g., "gpt-4o", "deepseek/deepseek-r1:free")
  - `agentargs`: Arguments for a custom agent (if not using a built-in model)

- **Task Selection**
  - `task_name`: Specific task name to run (e.g., "webclones.omnizon-1")
  - `task_type`: Task type to run (e.g., "omnizon")
  - `task_id`: Specific task ID within a task type

- **Leaderboard Settings**
  - `leaderboard`: Flag indicating whether to submit results to a leaderboard
  - `run_id`: Identifier for this run (required for leaderboard submission)

- **Browser Configuration**
  - `headless`: Whether to run the browser in headless mode
  - `max_steps`: Maximum number of steps per task
  - `use_html`: Whether to include HTML in observations
  - `use_axtree`: Whether to include accessibility tree in observations
  - `use_screenshot`: Whether to include screenshots in observations
  - `browser_dimensions`: Tuple of (width, height) for browser viewport
  - `golden_user_data_dir`: Path to browser user data directory
  - `extensions_dir`: Path to Chrome extensions directory
  - `viewport`: Dictionary with width and height for browser viewport

- **Execution Settings**
  - `results_dir`: Directory to store results
  - `parallel`: Whether to run tasks in parallel
  - `num_workers`: Number of parallel workers
  - `use_cache`: Whether to use cached results
  - `cache_only`: Only use cached results, don't run missing tasks
  - `force_refresh`: Force re-running tasks even if cached results exist

## Core Features

### Task Management

The harness provides methods for:
- Selecting tasks based on task type or specific task names
- Sampling random tasks for benchmarking
- Supporting both single and multi-task execution

### Agent Integration

The harness supports:
- Built-in agents using specified models (like GPT-4o)
- Custom agents that implement the `Agent` interface
- Automatic agent selection based on model name or custom arguments

### Caching System

The caching system helps avoid redundant computation:

1. **Cache Key Generation**
   - Each task-agent combination generates a unique cache key
   - Cache keys include: `{task_name}_{agent_type}_{model_name}_{max_steps}`
   - Leaderboard runs append `_leaderboard` to cache keys for separation

2. **Cache Storage**
   - Experiment results are stored in the results directory
   - Each experiment directory contains a `summary_info.json` with metadata
   - Metadata includes the cache key, task name, agent type, model name, etc.

3. **Cache Lookup**
   - Before running a task, the system checks for cached results with matching cache keys
   - Only uses cached results from leaderboard runs for new leaderboard submissions
   - Results with errors are never cached to prevent propagating failures

4. **Cache Control**
   - `use_cache`: Enable/disable using cached results
   - `cache_only`: Only use cached results, don't run missing tasks
   - `force_refresh`: Force re-running tasks even if cached results exist

### Parallel Execution

For running multiple tasks efficiently:

- `parallel`: Enable parallel execution using Python's multiprocessing
- `num_workers`: Control the number of parallel workers
- Automatically distributes tasks across available workers

### Leaderboard Integration

For submitting results to evaluation leaderboards:

- `leaderboard`: Flag indicating whether to submit results to a leaderboard
- `run_id`: Unique identifier for tracking leaderboard submissions
- Proper environment variable setup for leaderboard submissions
- Special caching behavior that separates leaderboard and development runs

## Usage Examples

### Basic Usage with Built-in Agent

```python
from agisdk import REAL

# Create a harness with a built-in agent using GPT-4o
harness = REAL.harness(
    model="gpt-4o",
    task_name="webclones.omnizon-1",  # Specific task
    headless=False,                   # Show browser window
    max_steps=25,                     # Maximum steps per task
    use_screenshot=True,              # Include screenshots in observations
    use_axtree=True,                  # Include accessibility tree
)

# Run the task and get results
results = harness.run()
```

### Using a Custom Agent

```python
from agisdk import REAL

# Create harness with custom agent
harness = REAL.harness(
    agentargs=YourCustomAgentArgs(),
    headless=False,
)

# Run the task
results = harness.run()
```

### Using OpenRouter with Deepseek R1

```python
from agisdk import REAL

# Create harness with OpenRouter agent for Deepseek R1
harness = REAL.harness(
    agentargs=OpenRouterAgentArgs(
        model_name="deepseek/deepseek-r1:free",
    ),
    task_name="webclones.omnizon-1",
    headless=False,
    max_steps=25,
    use_screenshot=True,
    use_axtree=True,
)

# Run the task
results = harness.run()
```

### Leaderboard Submission

```python
from agisdk import REAL

# Create a harness for leaderboard submission
harness = REAL.harness(
    model="gpt-4o-mini",
    leaderboard=True,
    run_id="your-unique-run-id",    # Your unique run ID for the leaderboard
    headless=True,                  # Run headless for submissions
    parallel=True,                  # Run tasks in parallel
    num_workers=20,                 # Number of parallel workers
)

# Run all available tasks
results = harness.run()
```

## Advanced Cache Control

The caching system can be controlled in several ways:

```python
# No caching - always run tasks
harness = REAL.harness(
    model="gpt-4o",
    use_cache=False
)

# Cache-only mode - only use cached results, don't run missing tasks
harness = REAL.harness(
    model="gpt-4o",
    cache_only=True
)

# Force refresh - run all tasks even if cached results exist
harness = REAL.harness(
    model="gpt-4o",
    force_refresh=True
)
```

## Working with Leaderboard Caching

Leaderboard runs maintain a separate cache from development runs:

```python
# For a leaderboard run (uses and creates leaderboard-specific cache)
harness = REAL.harness(
    model="gpt-4o",
    leaderboard=True,
    run_id="your-unique-run-id",
)

# For a development run (uses and creates non-leaderboard cache)
harness = REAL.harness(
    model="gpt-4o",
    leaderboard=False,
)
```

## Internal Flow

1. **Initialization**: Set up agent args, environment args, and other settings
2. **Task Selection**: Determine which tasks to run based on task_name, task_type, etc.
3. **Cache Lookup**: Check if there are cached results for the tasks
4. **Task Execution**: Run tasks that aren't in the cache or need re-running
5. **Result Collection**: Aggregate results from both cache and new runs
6. **Result Formatting**: Format and display the final results

## Extending the Harness

To extend the harness:

1. Create a custom agent by inheriting from `REAL.Agent`
2. Create agent arguments by inheriting from `REAL.AbstractAgentArgs`
3. Use your custom agent with the harness via `agentargs`

## Tips for Effective Use

- Use `use_cache=True` during development to speed up iteration
- Use `headless=False` when you want to visualize browser actions
- Use `leaderboard=True` and provide a `run_id` for leaderboard submissions
- Set appropriate `max_steps` to avoid excessively long runs
- Consider lower `max_steps` during development and higher for final evaluation
- Use `parallel=True` with an appropriate `num_workers` when running multiple tasks
