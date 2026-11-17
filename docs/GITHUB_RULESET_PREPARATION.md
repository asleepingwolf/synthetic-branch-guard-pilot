# GitHub ruleset preparation (proposal; NOT YET APPLIED)

## Repository creation

1. Create a **new public** GitHub repository (suggested name: `synthetic-branch-guard-pilot`).
2. Keep it separate from any private project. Do not use a template from a private repo, transfer source, copy history, add credentials, install apps, or invite automation accounts.
3. Choose the default branch `main` and upload the files from this package.

## Proposed rules: `main`

In repository **Settings → Rules → Rulesets**, prepare a branch ruleset targeting only the default branch `main`. For the narrow initial pilot:

- Enforcement: Active only once the owner confirms the target and bypass list.
- Require a pull request before merging.
- Block force pushes and deletion of `main`.
- Require a review approval (subject to availability and review identities); do not claim this is a distinct-owner merge restriction.
- If available, dismiss stale approvals after new commits and require approval of the latest reviewable push.
- Do not add any agent, bot, or GitHub App to a bypass list.
- Examine `Restrict updates` and PR-only bypass together, carefully: a too-restrictive combination can block the owner from merging, while a broad bypass can defeat the intended protection. Do not claim a policy is secure until negative tests verify it.
- Do not mark a status check as required unless a trusted check actually exists; this package intentionally contains **no GitHub Actions workflow**, so no checks have been registered.

Record the exact UI choices, bypass actors, public/private status, and effective ruleset URL in an owner's verification note. GitHub UI labels and plan capabilities can change.

## Permission boundary

- No collaborators, installed agent applications, workflow credentials, repository secrets, or model API calls during preparation.
- No tests against push/merge restrictions or bot identities until a **separate explicit approval**.
- Do not reuse personal GitHub tokens or owners' credentials in future agent jobs.
- Do not assume these rules are equivalent to a technical guarantee that only the owner can merge; negative tests and authorization checks must prove the guarantee.

## Future test ideas (NOT authorized)

1. Verify effective protection via a non-admin identity with a narrowly scoped permission.
2. Attempt direct push to `main` and verify server-side rejection.
3. Attempt merge after approvals and verify agent identity still cannot merge.
4. Verify owner path and rollback.
5. Measure model usage only after a separate real AI start-and-spend mandate.
