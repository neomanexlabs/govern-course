# Acme Billing: notes for AI agents

Everyone on the team adds to this file. Read all of it before you start.

## About the product

Acme Billing sends invoices for small shops: bakeries, florists, repair shops, a few cafés. A shop owner adds customers, creates invoices, sends them by email and records payments. Most shops send between 20 and 200 invoices a month. The biggest customer is Northside Florists with about 900 invoices a month. Customers mostly use the web app; a few use the CSV import.

The team is six developers: Priya (lead), Sam, Leo, Mina, Tom and Ana. Priya reviews anything that touches money. Leo owns deploys. Mina owns the email templates. Tom handles the CSV import. Ana joined in March and works on reports.

## Setup

- Python 3.12. Use a virtualenv. Do not install packages globally.
- Run `pip install -r requirements.txt` if a requirements file exists. There is none yet; pytest is enough.
- The code lives in `billing/`. Tests live in `tests/`. Docs live in `docs/`.
- Run the tests with `python3 -m pytest -q`.
- If pytest is missing, install it in the virtualenv.
- Do not commit the virtualenv.
- Do not commit `.pytest_cache` or `__pycache__`.
- macOS and Linux both work. Nobody has tried Windows.

## Code style

- Follow PEP 8.
- Use type hints on public functions.
- Prefer dataclasses for simple records.
- Keep functions short. If a function needs a comment to explain what it does, split it.
- No wildcard imports.
- Name things for what they are, not for how they are used.
- Use f-strings, not `%` or `.format()`.
- Sort imports: standard library, third party, local.
- Line length 100.
- Docstrings on public classes. One line is fine.
- Do not leave commented-out code.
- Do not leave `print` statements. Use logging if you need output.
- Constants in UPPER_CASE at the top of the module.
- Avoid clever one-liners. Write it so Ana can read it.

## Git

- Branch from `main`.
- Branch names: `fix/<short-name>`, `feat/<short-name>`, `chore/<short-name>`.
- Commit messages: imperative mood, under 72 characters in the first line.
- Reference the invoice or ticket number when there is one.
- Do not force-push `main`.
- Rebase your branch on `main` before opening a pull request.
- Squash fixup commits before review.
- Tag releases `vYYYY.MM.DD`.

## Pull requests

- One change per pull request.
- Write what changed and why in the description.
- Add screenshots for anything visible in the web app.
- Link the ticket.
- Priya reviews money changes. Anyone can review the rest.
- Do not merge your own pull request unless it is a typo fix.
- If CI is red, do not merge.
- Keep pull requests under 400 lines where you can.

## Money

- Money is `Decimal`, never `float`.
- Round to cents with `ROUND_HALF_UP`, only at the end of a calculation.
- The tax rate is 20% for now. It lives in `billing/invoice.py` as `TAX_RATE`.
- Totals are subtotal plus tax.
- Never round line amounts before summing them.
- Currency is EUR for every shop today. Do not assume it stays that way.
- Show amounts with two decimals.
- Negative amounts are credit notes. We do not support them yet.

## Invoices

- An invoice has an id like `INV-2040`, a list of lines and a status.
- A line has a description, a quantity and a unit price.
- Statuses: draft, sent, paid, void.
- A sent invoice is never edited. Void it and send a new one.
- Invoice numbers never repeat, even after a void.
- The PDF layout is in the web app, not in this repo.
- Due date is 30 days after the send date unless the shop sets another term.

## Customers

- Customer records hold a name, an email and an optional VAT number.
- Never log a customer's email address.
- Never put customer data in test fixtures. Use made-up names.
- A shop can have up to 5,000 customers. Nobody has more than 1,200 today.
- Deleting a customer keeps their invoices.

## Email

- Mina owns the templates. Ask before changing them.
- Plain text and HTML versions both exist for every email.
- Subjects stay under 60 characters.
- Never send a real email from a test.
- The sender is `billing@example.com` in every environment except production.

## CSV import

- Tom owns the importer.
- The importer accepts UTF-8 only.
- Dates in the CSV are `YYYY-MM-DD`.
- A failed row does not stop the import; it goes in the error report.
- Keep the column order stable. Shops have scripts that depend on it.

## Reports

- Ana owns reports.
- Monthly revenue report sums paid invoices by payment date, not send date.
- Reports run at 02:00 server time.
- Do not add a report without asking Ana.

## Testing

- Tests use pytest.
- One test file per module.
- Use plain `assert`.
- Keep fixtures small.
- Every bug fix ships with a test that fails before the fix and passes after it.
- Do not mock the invoice maths. Test it for real.
- Tests must not touch the network.
- Tests must run in under 10 seconds in total.
- Name tests for the behaviour: `test_total_includes_tax`, not `test_1`.

## Deploys

- Leo owns deploys.
- Deploys happen Tuesday and Thursday mornings.
- Never deploy on a Friday.
- A deploy needs a green `main`.
- Roll back first, investigate after.
- Announce deploys in the team channel.
- Database migrations go out in their own deploy.

## Errors and logging

- Log at INFO for business events: invoice sent, payment recorded.
- Log at WARNING for anything a shop owner might notice.
- Log at ERROR only for things someone must fix.
- Never log amounts together with customer names.
- Include the invoice id in every invoice log line.

## Performance

- Invoice totals must compute in under 5 ms for 500 lines.
- The invoice list page loads 50 invoices at a time.
- Do not load all invoices of a shop into memory.

## Security

- Never commit secrets.
- The API keys live in the deploy environment, not in the repo.
- Check that the shop owns an invoice before showing it.
- Escape everything that goes into HTML.

## Incidents we learned from

- 2025-11: an invoice showed a total with three decimals. We now round only at the end.
- 2026-01: a CSV with Windows line endings broke the importer. Tom fixed it.
- 2026-02: a reminder email went out twice. Mina added a sent flag.
- 2026-04: a report double-counted a payment recorded twice. Ana added a unique key.
- 2026-05: a deploy on a Friday broke the invoice list over the weekend. No Friday deploys.
- 2026-06: a float crept into a discount calculation. Money is Decimal.

## Working with the agent

- Explain what you changed in plain words when you finish.
- Ask before deleting files.
- Ask before changing more than three files.
- Do not reformat files you did not change.
- Do not upgrade dependencies unless asked.
- If something is unclear, ask.
- When you finish, run the tests.
- Keep your answers short.

## Misc

- The office is closed on public holidays. Nobody deploys then.
- The design system for the web app is in another repo.
- The support inbox is watched by Priya and Sam.
- Northside Florists get a call before any change to the invoice email.
- The logo files are in the web app repo.
- We use UTC in the database and local time on screen.
- Old invoices before 2024 were migrated from spreadsheets; some have odd descriptions. Leave them.
