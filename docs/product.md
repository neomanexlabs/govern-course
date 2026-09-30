# The product

Acme Billing sends invoices for small shops: bakeries, florists, repair shops, a few cafés. A shop owner adds customers, creates invoices, sends them by email and records payments. Most shops send between 20 and 200 invoices a month. The biggest customer is Northside Florists with about 900 invoices a month. Customers mostly use the web app; a few use the CSV import.

The team is six developers: Priya (lead), Sam, Leo, Mina, Tom and Ana. Priya reviews anything that touches money. Leo owns deploys. Mina owns the email templates. Tom handles the CSV import. Ana joined in March and works on reports.

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
