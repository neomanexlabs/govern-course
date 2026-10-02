# Invoicing

What an invoice is and how it behaves. The code is `billing/invoice.py`.

- An invoice has an id like `INV-2040`, a list of lines and a status.
- A line has a description, a quantity and a unit price.
- Quantities are not always whole numbers. Repair shops bill labour by the hour, in quarter hours: `0.25`, `1.5`, `2.75`.
- Statuses: draft, sent, paid, void.
- A sent invoice is never edited. Void it and send a new one.
- Invoice numbers never repeat, even after a void.
- The PDF layout is in the web app, not in this repo.
- Due date is 30 days after the send date unless the shop sets another term.

## Known issues

- Invoice `INV-2040` shows the wrong total (reported by customers). Not fixed yet.
