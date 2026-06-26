import os

from pathlib import Path
from backend.engine.engine import Engine
from backend.engine.config import Config

# export OPENAI_API_KEY=sk-your-key-here

SCRIPT_DIR = Path(__file__).parent

engine_config = Config(
    default_model_id="gpt-4o",
    tools_dir=str(SCRIPT_DIR.parent / "tools"),
    mcp_tools_dir=str(SCRIPT_DIR.parent / "mcp_tools"),
    memory_dir=str(SCRIPT_DIR.parent.parent / "memory"),
    provider_config={
        "openai": {
            "api_key": os.environ["OPENAI_API_KEY"],
            "base_url": None,
            "default_model": "gpt-4o"
        }
    }
)


# Input functioon to get user input
def on_user_input_func():
    try:
        return input("You: ") # Accept user input from the console
    except EOFError:
        return None

def on_tool_call_func(tool_name: str, arguments: dict, tool_call_result: str):
    print(f"Tool call made: {tool_name} with arguments: {arguments} and result: {tool_call_result}")

def on_response_func(response):
    print(f"Final response from the Agent: {response}")


# Initialize the Engine with the configuration and callback functions
engine = Engine(engine_config)

if __name__ == "__main__":
        engine.run(
                get_input_func=on_user_input_func,
                on_tool_call_func=on_tool_call_func,
                on_response_func=on_response_func
        ) 