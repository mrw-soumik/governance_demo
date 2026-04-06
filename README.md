# Governance Demo – Startup Project Example

## Problem Statement

Early-stage startups often move fast and rely on contractors to build initial systems.
That can create governance risks such as:

- code stored in personal repositories
- no clear ownership
- manual deployment steps
- limited documentation
- heavy dependency on one developer

These risks make the system harder to maintain, scale, and transfer.

## Solution

This repository demonstrates a small, well-governed startup-style backend project with:

- company-owned repository
- visible version history
- automated CI pipeline
- clear project structure
- simple documentation

The goal is to show how development governance reduces contractor risk.

## Project Overview

This is a small FastAPI service that manages a few sample startup projects.

### Features
- health check endpoint
- list projects endpoint
- filter projects by status
- automated tests
- GitHub Actions CI workflow

## API Endpoints

### `GET /`
Returns service information.

### `GET /health`
Returns service health.

### `GET /projects`
Returns all sample projects.

### `GET /projects?status=active`
Returns only projects matching a given status.

## Governance Controls Demonstrated

1. **Repository Ownership**  
   The repository should be pushed to a company or organization GitHub account.

2. **Version History**  
   Every change is tracked through commits.

3. **Automated Validation**  
   Tests run automatically on every push through GitHub Actions.

4. **Clear Documentation**  
   The structure and purpose of the project are easy to understand.

## Project Structure

```text
app/
  main.py
tests/
  test_main.py
.github/
  workflows/
    ci.yml
requirements.txt
README.md
```

## Local Setup

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/docs

## Run Tests

```bash
pytest
```

## Demo Purpose

Use this repository in presentations to show:

- company ownership of code
- commit history
- CI pipeline
- practical governance controls
