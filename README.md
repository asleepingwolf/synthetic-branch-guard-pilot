# Synthetic Branch Protection Pilot

This repository contains only synthetic example code and documentation. It is not connected to any private project, credentials, services, or AI agents.

## Scope

- Prepare a public GitHub repository on GitHub Free.
- Configure GitHub-native protection for `main`.
- Do not install apps, attach model providers, add secrets, or trigger workflows as part of preparation.
- Permission and merge-denial tests are explicitly **out of scope** until separately approved.

## Synthetic code

`calculator.py` provides a tiny deterministic `add()` function. `tests/test_calculator.py` is a plain unittest test file. These files do not make network calls or use credentials.

## Local test (optional, no third-party packages)

```bash
python -m unittest discover -s tests -v
```

See `docs/GITHUB_RULESET_PREPARATION.md` for the proposed repository rules. Apply settings as a separate, deliberate repository-owner action. Do not grant agent access.
