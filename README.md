summarizer-service

TL;DR: A FastAPI service that will summarize documents with an LLM. Right now it's the production skeleton: typed Python, tests, linting, secret scanning, and CI on every push. LLM calls arrive in week 3.

Quick start
bash
git clone https://github.com/sachindongare11/summarizer-service.git
cd summarizer-service
uv sync --all-groups
cp .env.example .env          # then add your real values to .env
uv run uvicorn summarizer_service.main:app --reload
Health check: http://127.0.0.1:8000/health
API docs: http://127.0.0.1:8000/docs
Checks (same as CI)
bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv run pytest -v
Structure
src/summarizer_service/
├── main.py     # FastAPI app and routes
├── config.py   # settings loaded from environment
├── models.py   # request/response schemas
└── llm.py      # LLM client and test fakes
tests/          # pytest suite
Decisions
uv + lockfile: uv.lock pins every package version, so laptop, CI and Docker install the same thing.
src/ layout: the package is installed, not imported from the working folder, so tests can't pass by accident.
Strict mypy + Ruff: type and lint errors fail CI, so reviews focus on logic.
Secrets stay out of Git: real values live in .env (ignored). .env.example holds placeholders only. Gitleaks runs as a pre-commit hook.
Pinned CI runner (ubuntu-24.04): the OS image can't change under the build without a commit.
