from . import browsergym
from . import tasks
from .harness import harness, Agent, AbstractAgentArgs

def hello(name="World"):
    """A real greeting function for the real submodule."""
    message = f"Hello {name}, from the real world!"
    print("nothing change")
    print(message)
    return message