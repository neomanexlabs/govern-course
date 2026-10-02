# Security and customer data

At most 15 rules. To add one, retire one (`workflows/cap-and-retire.md`).

## Security

- Never commit secrets.
- The API keys live in the deploy environment, not in the repo.
- Check that the shop owns an invoice before showing it.
- Escape everything that goes into HTML.

## Customer data

- Never log a customer's email address.
- Never put customer data in test fixtures. Use made-up names.
