from . import core, utils, webclones

from .experiments.agent import Agent, AgentInfo
from .experiments.loop import (
    EnvArgs,
    ExpArgs,
    AbstractAgentArgs,
    ExpResult,
    StepInfo,
    StepTimestamps,
)
from .core.action.base import AbstractActionSet
from .core.action.highlevel import HighLevelActionSet
from .core.action.python import PythonActionSet



def hello(name="World"):
    """A real greeting function for the browsergym real submodule."""
    message = f"Hello {name}, from the browsergym real world!"
    print(message)
    return message