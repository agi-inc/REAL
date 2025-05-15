# AGI SDK Examples

This directory contains example implementations demonstrating how to use the AGI SDK for building and testing web agents. Each example showcases different approaches to agent implementation and configuration.

## Available Examples

### 1. `starter.py`

The simplest agent implementation that works with any model. This is the best starting point for beginners.

**Features:**
- Minimal implementation that works with any supported model
- Multiple configuration options for flexibility
- Easy to understand and modify

**How to run:**
```bash
# Run with default settings
python starter.py

# Run with custom model or configuration
python starter.py --model gpt-4o --task webclones.omnizon-1 --headless False
```

### 2. `custom.py`

Boilerplate code for creating your own custom agent. Use this as a template when implementing your own agent logic.

**Features:**
- Basic structure for a custom agent implementation
- Minimal code needed to get started
- Clear instructions for extending functionality

**How to run:**
```bash
# Run the custom agent example
python custom.py
```

### 3. `hackable.py`

A more advanced, feature-rich agent implementation designed for others to use and improve. This is our recommended agent for most use cases.

**Features:**
- Detailed agent implementation with observation preprocessing
- Support for different model backends (OpenAI, Anthropic, OpenRouter)
- Configurable agent parameters via command-line arguments
- Extensive documentation and examples

**How to run:**
```bash
# Run with default configuration
python hackable.py

# Run with custom parameters
python hackable.py --model gpt-4o --task webclones.omnizon-1 --headless False --leaderboard True --run_id your-run-id
```

### 4. `nova.py`

Designed for cases where the agent needs to own its own browser. This example demonstrates integration with Nova-Act by Amazon.

**Features:**
- Direct Playwright browser control
- Configurable routes and task IDs
- Automatic submission of results

**How to run:**
```bash
# Before running, update the run_id in the script
# Edit line 6: run_id = "YOUR-UUID-HERE" with your actual run ID
python nova.py
```

## Harness Configuration

Most examples use the REAL harness, which accepts various configuration parameters:

```python
REAL.harness(
    # Agent configuration (provide one of these)
    model="gpt-4o",                                # OpenAI models
    model="sonnet-3.7",                            # Anthropic models
    model="openrouter/deepseek/deepseek-r1:free",    # OpenRouter models (Deepseek R1)
    agentargs=MyAgentArgs(),                       # Or custom agent arguments

    # Task selection (provide one of these)
    task_name="webclones.omnizon-1",  # Specific task to run
    task_type="omnizon",              # Run all tasks of this type
    task_id=1,                        # Run specific task ID within a type

    # Browser configuration
    headless=False,                   # Whether to show the browser
    max_steps=25,                     # Maximum number of steps
    
    # Observation options
    use_html=False,                   # Include HTML in observations
    use_axtree=True,                  # Include accessibility tree
    use_screenshot=True,              # Include screenshots

    # Leaderboard submission
    leaderboard=False,                # Whether to submit to leaderboard
    run_id="my_unique_id",            # Unique ID for the submission

    # Execution options
    parallel=False,                   # Run tasks in parallel
    num_workers=4,                    # Number of parallel workers
)
```

## Creating Your Own Agent

To create your own agent:

1. Subclass `REAL.Agent` and implement the required methods:
   - `__init__`: Initialize your agent
   - `get_action`: Process observations and return actions

2. Create an arguments class by subclassing `REAL.AbstractAgentArgs`

3. Use your agent with the harness:
   ```python
   harness = REAL.harness(
       agentargs=YourCustomAgentArgs(),
       # other configuration options
   )
   ```

See the `MyCustomAgent` class in `custom.py` or the `DemoAgent` class in `hackable.py` for implementation examples.

## Using Different Models

The AGI SDK supports various model providers:

- **OpenAI**: Set `model="gpt-4o"` or other OpenAI models
- **Anthropic**: Set `model="sonnet-3.7"` or other Anthropic models
- **OpenRouter**: Set `model="openrouter/deepseek/deepseek-r1:free"` for Deepseek R1 or other models

Make sure you have the appropriate API keys set in your environment variables:

```bash
# For OpenAI models
export OPENAI_API_KEY="your-openai-api-key"

# For Anthropic models
export ANTHROPIC_API_KEY="your-anthropic-api-key"

# For OpenRouter models
export OPENROUTER_API_KEY="your-openrouter-api-key"
```
