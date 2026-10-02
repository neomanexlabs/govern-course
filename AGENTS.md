# Acme Billing

Invoicing for small shops. Python 3.12, pytest. Run the tests: `python -m pytest -q`

This file stays under 200 words. To add a line, retire one (`workflows/cap-and-retire.md`).

## Every change

- Bug fix: follow `workflows/bug-fix.md`, every step, in order.
- Money is `Decimal`, never `float`.
- Never commit with a failing test.
- Never commit secrets or customer data.
- Before you change code, start the pull request description from `.github/pull_request_template.md` and fill in "Standards followed". The review checks the change against that list.
- Last step: if the change makes a doc in `docs/` wrong or incomplete, update it in the same commit.

## Before you work on it, read

| Work on | Read |
|---|---|
| tests | `standards/testing.md` |
| money, totals, tax | `standards/money.md` |
| any code | `standards/code-style.md` |
| commits, branches, pull requests | `standards/git.md` |
| logs and errors | `standards/logging.md` |
| security, customer data | `standards/security.md` |
| speed | `standards/performance.md` |
| invoices, lines, totals | `docs/invoicing.md` |
| customers, email, CSV, reports | `docs/product.md` |
| setup, deploys, past incidents, team notes | `docs/` |
