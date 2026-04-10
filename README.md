# AI Code Agent

An automated, terminal-based AI coding assistant powered by the Gemini API. This agent is designed to autonomously interact with the local file system to read, write, and execute Python code, accelerating development and refactoring workflows.

## Features

* **LLM Integration:** Seamlessly interfaces with the Gemini API to process prompts and generate accurate code suggestions.
* **File System Operations:** Capable of reading directory structures (`get_files_info`), extracting file contents (`get_file_content`), and writing updates directly to disk (`write_file`).
* **Code Execution:** Includes built-in functionality to securely run Python scripts (`run_python_file`) and return output directly to the agent.
* **Extensible Architecture:** Modular design separates core LLM config, prompt engineering, and distinct tool functions, making it highly scalable for future integrations.

## Tech Stack

* **Language:** Python
* **Package Manager:** [uv](https://github.com/astral-sh/uv) (for fast, reliable dependency resolution)
* **AI Provider:** Google Gemini API

## Getting Started

### Prerequisites

* Python 3.10+
* `uv` installed on your machine
* A valid Gemini API key

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/md-173/ai-code-agent.git](https://github.com/md-173/ai-code-agent.git)
   cd ai-code-agent
   ```

2. **Install dependencies using uv:**
   ```bash
   uv sync
   ```

3. **Set up environment variables:**
   Create a `.env` file in the root directory and add your API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

Run the main agent script to start the interactive session:
```bash
uv run main.py
```

## Testing

This project utilizes a suite of unit tests to ensure the reliability of file operations and code execution tools. To run the tests, execute:
```bash
uv run pytest
```
*Current test coverage includes `test_get_file_content.py`, `test_get_files_info.py`, `test_run_python_file.py`, and `test_write_file.py`.*

## Project Structure

* `main.py`: The entry point for the agent loop.
* `config.py`: Configuration and environment variable management.
* `prompts.py`: System prompts and context-handling logic.
* `call_function.py`: Tool orchestration logic linking the LLM to local functions.
* `functions/`: Core tool implementations for file and execution tasks.
