import config
import prompts
import os

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
CHECK = "✔"
CROSS = "❌"

def test_main_runs():
    try:
        import main
        print(f"{GREEN}{CHECK} Main import successful{RESET}")
    except Exception as e:
        print(f"{RED}{CROSS} Error during main import: {e}{RESET}")

def test_config_values():
    if not isinstance(config.MAX_CHARS, int):
        print(f"{RED}{CROSS} MAX_CHARS is not an integer{RESET}")
    else:
        print(f"{GREEN}{CHECK} MAX_CHARS check passed{RESET}")

    if not isinstance(config.WORKING_DIR, str):
        print(f"{RED}{CROSS} WORKING_DIR is not a string{RESET}")
    else:
        print(f"{GREEN}{CHECK} WORKING_DIR check passed{RESET}")

    if not isinstance(config.MAX_ITERS, int):
        print(f"{RED}{CROSS} MAX_ITERS is not an integer{RESET}")
    else:
        print(f"{GREEN}{CHECK} MAX_ITERS check passed{RESET}")

def test_prompts():
    prompt = prompts.system_prompt
    if not prompt:
        print(f"{RED}{CROSS} System prompt is empty{RESET}")
    elif not isinstance(prompt, str):
        print(f"{RED}{CROSS} System prompt is not a string{RESET}")
    else:
        print(f"{GREEN}{CHECK} System prompt check passed{RESET}")

def test_env_vars_loaded():
    if not os.environ.get("GEMINI_API_KEY"):
        print(f"{RED}{CROSS} GEMINI_API_KEY environment variable is not set{RESET}")
    else:
        print(f"{GREEN}{CHECK} GEMINI_API_KEY environment variable check passed{RESET}")

test_main_runs()
test_config_values()
test_prompts()
test_env_vars_loaded()
