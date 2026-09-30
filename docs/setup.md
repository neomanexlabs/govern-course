# Setup

- Python 3.12. Use a virtualenv. Do not install packages globally.
- Run `pip install -r requirements.txt` if a requirements file exists. There is none yet; pytest is enough.
- The code lives in `billing/`. Tests live in `tests/`. Docs live in `docs/`.
- Run the tests with `python3 -m pytest -q`.
- If pytest is missing, install it in the virtualenv.
- Do not commit the virtualenv.
- Do not commit `.pytest_cache` or `__pycache__`.
- macOS and Linux both work. Nobody has tried Windows.
