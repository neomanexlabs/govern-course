# Performance

At most 15 rules. To add one, retire one (`workflows/cap-and-retire.md`).

- Invoice totals must compute in under 5 ms for 500 lines.
- The invoice list page loads 50 invoices at a time.
- Do not load all invoices of a shop into memory.
