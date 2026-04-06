# Governance Demo - Startup Project Example

A small FastAPI repository designed for presentations and training demos about
development governance in early-stage startups.

## Why this repo exists

Startups often move quickly, use contractors, and postpone process controls.
That creates predictable risks:

- code lives in a personal account
- ownership is unclear
- changes are pushed without review
- deployments depend on one developer
- documentation is thin

This repository turns those risks into something concrete that you can show:
visible ownership metadata, review expectations, automated validation, and a
small codebase that is easy to understand in a live demo.

## What this project does

The app is intentionally small. It exposes a few FastAPI endpoints that return
sample startup project data:

- `GET /` returns service metadata
- `GET /health` returns a simple health response
- `GET /projects` lists sample projects
- `GET /projects?status=active` filters by project status

## Governance controls included in the repo

- Code ownership: [`.github/CODEOWNERS`](.github/CODEOWNERS)
- Contribution and review expectations: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Pull request checklist: [`.github/pull_request_template.md`](.github/pull_request_template.md)
- Automated validation: [`.github/workflows/ci.yml`](.github/workflows/ci.yml)
- Security reporting guidance: [`SECURITY.md`](SECURITY.md)
- Presentation and settings checklist: [`docs/github-governance-checklist.md`](docs/github-governance-checklist.md)

## Important accuracy note

This repository currently lives in a personal GitHub account. Before you
present it as a company-owned engineering asset, transfer it to a GitHub
organization or company-owned repository and apply the checklist in
[`docs/github-governance-checklist.md`](docs/github-governance-checklist.md).

That distinction matters. Governance claims should match the actual repository
settings, not just the README text.

## Project structure

```text
app/
  main.py
tests/
  test_main.py
.github/
  CODEOWNERS
  pull_request_template.md
  workflows/
    ci.yml
docs/
  github-governance-checklist.md
  presentation-walkthrough.md
requirements.txt
pytest.ini
README.md
CONTRIBUTING.md
SECURITY.md
```

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/docs

## Run tests

```bash
pytest
```

## Demo talking points

- The code is small enough to understand quickly.
- Ownership and review rules are visible in the repository.
- Every push and pull request runs automated checks.
- The remaining controls that live in GitHub settings are documented and can be
  enabled before the presentation.
