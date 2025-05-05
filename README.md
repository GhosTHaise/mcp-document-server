# Astral Project with uv

This project uses [uv](https://github.com/astral-sh/uv), a fast Python package manager created by Astral. `uv` is a drop-in replacement for `pip`, `pip-tools`, and `virtualenv`, designed to be much faster.

## Requirements

- Python 3.8+
- `uv` installed

## Installation

First, install `uv` if you haven’t already:

```bash
curl -Ls https://astral.sh/uv/install.sh | sh

Or use pipx:

pipx install uv

Creating a Virtual Environment

Create a virtual environment with uv:

uv venv .venv

Activate it:
	•	On Linux/macOS:

source .venv/bin/activate


	•	On Windows:

.venv\Scripts\activate



Installing Dependencies

Install the packages listed in requirements.txt (or pyproject.toml if you’re using modern packaging):

uv pip install -r requirements.txt

Or if using pyproject.toml:

uv pip install .

Adding a New Package

To add a new package:

uv pip install package-name

Freezing Dependencies

Freeze the current environment packages into requirements.txt:

uv pip freeze > requirements.txt

Why uv?
	•	Much faster than traditional pip and virtualenv
	•	Manages virtual environments and packages in one tool
	•	Built by Astral

Happy coding!

Would you also like a French version alongside it (like a bilingual `README.md`)?  
Or maybe you want a smaller **minimal version**?