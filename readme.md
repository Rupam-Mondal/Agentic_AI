# Vitual Environment (01_basics) 

A virtual environment (venv) is like a separate box for a Python project.

Each project can have its own Python version

Each project can have its own libraries & versions

Prevents dependency conflicts

👉 Example problem without venv:
Project A needs Django 3.2
Project B needs Django 4.2
Both will clash if installed globally ❌

- `python -m venv .venv(name)`
- `.venv\Scripts\activate`

Under main folder You can create `requirements.txt`
- `pip install -r requirements.txt`
everything inside this will be installed.