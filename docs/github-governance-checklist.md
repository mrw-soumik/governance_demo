# GitHub Governance Checklist

Use this checklist before presenting the repository as evidence of governance
maturity. These controls live in GitHub settings, not just in repository files.

## 1. Transfer the repository to the right owner

- Move the repository into a GitHub organization or company-owned account.
- Confirm at least two maintainers have admin access.
- Update [`.github/CODEOWNERS`](../.github/CODEOWNERS) to the real team handle.

## 2. Protect the default branch

Enable branch protection for `main` and require:

- pull requests before merge
- at least one reviewer
- required status checks before merge
- dismissal of stale approvals after new commits
- blocked force-pushes to `main`

## 3. Make CI a required control

- Mark the `CI` workflow as a required status check for `main`.
- Do not allow admins to bypass checks unless there is an explicit exception
  process.

## 4. Keep credentials and automation centralized

- Store secrets in GitHub organization or repository secrets, not in code.
- Use organization-owned service accounts where possible.
- Review GitHub Actions permissions and keep them as narrow as possible.

## 5. Make ownership visible

- Keep `README.md`, `CONTRIBUTING.md`, and `SECURITY.md` current.
- Make sure pull requests request the correct code owner automatically.
- Keep at least one backup maintainer in addition to the primary owner.

## 6. Show evidence during the demo

For a presentation, show these items live:

1. Repository owner and collaborators or organization membership
2. Commit history on `main`
3. Pull request template or contribution rules
4. A successful GitHub Actions run
5. Branch protection rules in repository settings
