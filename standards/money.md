# Money

- Money is `Decimal`, never `float`.
- Round to cents with `ROUND_HALF_UP`, only at the end of a calculation.
- The tax rate is 20% for now. It lives in `billing/invoice.py` as `TAX_RATE`.
- Totals are subtotal plus tax.
- Never round line amounts before summing them.
- Currency is EUR for every shop today. Do not assume it stays that way.
- Show amounts with two decimals.
- Negative amounts are credit notes. We do not support them yet.
