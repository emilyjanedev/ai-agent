# AI Code Assistant

This project is an AI-powered code assistant that uses the Gemini API to help you with coding tasks. It can understand natural language prompts and generate code, modify existing code, and run tests to ensure everything works as expected.

## Calculator Project Example

The `calculator` directory contains a simple calculator project that can be used as an example for testing the AI Code Assistant's capabilities. You can ask the assistant to add features, fix bugs, or refactor the code in the calculator project.

**Important:** The AI agent's working directory is hardcoded to the root of this project for security reasons. It cannot access files outside of this directory.

## Usage

To use the AI Code Assistant, run `main.py` with your prompt as a command-line argument:

```bash
python main.py "Your prompt here"
```

For example:

```bash
python main.py "How do I fix the calculator?"
```

You can also use the `--verbose` flag to see more detailed output:

```bash
python main.py "Add a square root function to the calculator" --verbose
```

## Installation

1.  Clone the repository.
2.  Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3.  Create a `.env` file by copying the contents of `.env.sample` and replacing `YOUR_API_KEY` with your actual Gemini API key:

    ```bash
    cp .env.sample .env
    # Then edit .env to set the correct API key
    ```

## Configuration

The `config.py` file contains configuration options for the project:

- `MAX_CHARS`: Maximum number of characters allowed in the model's response.
- `WORKING_DIR`: The working directory for the AI agent. This is currently set to the root of the calculator project.
- `MAX_ITERS`: Maximum number of iterations the AI agent will run for a given task.
