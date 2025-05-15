# BrowserGym Module Structure

This document provides an overview of the `browsergym` module structure and its key components.

## Overview

BrowserGym is a framework for training and evaluating AI agents on web browsing tasks. It provides a Gymnasium-compatible interface for browser automation, allowing agents to interact with web interfaces similar to how humans would.

## Module Structure

### `core/`

The core module contains fundamental components for browser automation:

- **action/**: Defines different action spaces for browser interaction
  - `base.py`: Base action space definitions
  - `functions.py`: Function-based actions
  - `highlevel.py`: High-level composite actions
  - `openai_cua.py`: OpenAI-compatible browser actions
  - `python.py`: Python-based control actions
  - `utils.py`: Helper utilities for actions

- **env.py**: Main `BrowserEnv` class implementing the Gymnasium interface

- **observation.py**: Handles extraction of browser state as agent observations

- **spaces.py**: Defines observation and action spaces

- **task.py**: Interface for defining browser-based tasks

- **chat.py**: Implements chat interface functionalities

- **javascript/**: JavaScript code for browser DOM manipulation

- **constants.py**: Constants used throughout the module

- **registration.py**: Functions for registering environments

### `experiments/`

This module provides infrastructure for running agents in the browser environment:

- **agent.py**: Abstract `Agent` class and implementations for browser interaction

- **loop.py**: Implements the experiment loop functionality

- **utils.py**: Utility functions for experiments

### `utils/`

Utility functions supporting the main functionality:

- **obs.py**: Utilities for processing observations

### `webclones/`

Implementation of benchmark tasks based on web interfaces:

- **base.py**: Base classes for web clone tasks

- **evaluate.py**: Evaluation functionality for web tasks

- **task_config.py**: Configuration for web tasks

- **tasks/**: JSON files defining various web-based tasks
  - Multiple task definitions organized by simulated website (e.g., dashdish, fly-unified, gocalendar)
  - Each JSON file contains a task definition with goals, success criteria, and other metadata

- **utils.py**: Utilities specific to web clone tasks

## Key Concepts

1. **BrowserEnv**: The main environment class that provides a Gymnasium-compatible interface to a browser

2. **Action Spaces**: Different ways agents can interact with the browser (clicks, typing, scrolling, etc.)

3. **Observations**: Representations of browser state (DOM tree, accessibility tree, screenshots)

4. **Tasks**: Definitions of goals and success criteria for browser-based tasks

5. **Agents**: Implementations that can perceive browser state and decide on actions

6. **WebClone Tasks**: Benchmark tasks designed to evaluate agent performance on common web interfaces

## Usage

The BrowserGym module can be used to:

1. Define browser-based tasks
2. Implement and test agents that can perform these tasks
3. Evaluate agent performance across a range of web interfaces
4. Research and develop new approaches to web automation and understanding

For examples, see the example directory in the repository root.