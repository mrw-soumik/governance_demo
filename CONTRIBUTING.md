# Contributing

This repository is used to demonstrate basic development governance in a small
startup-style project. Changes should be small, reviewable, and traceable.

## Expected workflow

1. Branch from `main` for any non-trivial change.
2. Open a pull request instead of pushing directly to `main`.
3. Describe the change clearly, including any governance or operational impact.
4. Update tests and documentation when behavior changes.
5. Wait for CI to pass and for a code owner to review before merging.

## Review standard

- Keep pull requests focused on one purpose.
- Do not commit secrets, personal credentials, or local environment files.
- Document any new endpoint, dependency, or operational requirement.
- If a change affects ownership or deployment, update the relevant docs in the
  same pull request.

## Local validation

```bash
pip install -r requirements.txt
pytest
```

## Ownership

The default code owner is defined in [`.github/CODEOWNERS`](.github/CODEOWNERS).
If this repository is transferred to a company organization, update that file to
use the correct team or maintainer group.
