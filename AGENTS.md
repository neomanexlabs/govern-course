# Acme Billing

Invoicing for small shops. Python 3.12, pytest. Run the tests: `python -m pytest -q`

## Every change

- Bug fix: first write a test that shows the bug. Run it and see it fail. Then fix, then run the whole suite.
- Money is `Decimal`, never `float`.
- Never commit with a failing test.
- Never commit secrets or customer data.

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
| invoices, customers, email, CSV, reports | `docs/product.md` |
| setup, deploys, past incidents, team notes | `docs/` |
