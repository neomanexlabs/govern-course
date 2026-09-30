# Incidents we learned from

- 2025-11: an invoice showed a total with three decimals. We now round only at the end.
- 2026-01: a CSV with Windows line endings broke the importer. Tom fixed it.
- 2026-02: a reminder email went out twice. Mina added a sent flag.
- 2026-04: a report double-counted a payment recorded twice. Ana added a unique key.
- 2026-05: a deploy on a Friday broke the invoice list over the weekend. No Friday deploys.
- 2026-06: a float crept into a discount calculation. Money is Decimal.
