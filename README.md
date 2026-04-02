# SIH25

A minimal, production-minded bootstrap for a Python API service using only the standard library.

## What this includes

- Runnable API service (`app/main.py`)
- Health endpoint (`GET /health`)
- Unit/smoke tests with built-in `unittest`
- CI workflow for basic validation
- Environment template and contribution docs

## Quick start

```bash
python app/main.py
```

Then open: `http://localhost:8000/health`

## Run checks

```bash
python -m unittest discover -s tests -p 'test_*.py'
python -m compileall app tests
```

## Project structure

```text
app/
  main.py
tests/
.github/workflows/ci.yml
requirements.txt
requirements-dev.txt
```

## Environment variables

Copy `.env.example` to `.env` and adjust values as needed.
