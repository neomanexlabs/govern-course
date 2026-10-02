# Money

- Money is `Decimal`, never `float`.
- Round to cents with `ROUND_HALF_UP`, only at the end of a calculation.
- The tax rate is 20% for now. It lives in `billing/invoice.py` as `TAX_RATE`.
- An invoice shows subtotal, tax and total in cents, and they add up. The total is the unrounded subtotal plus its tax, rounded once. The subtotal shown is rounded on its own. The tax shown is the total minus the subtotal shown. (Why: two reviews of the INV-2040 fix read "only at the end" two ways.)
- Never round line amounts before summing them.
- Currency is EUR for every shop today. Do not assume it stays that way.
- Show amounts with two decimals.
- Negative amounts are credit notes. We do not support them yet.
