# Code style

At most 15 rules. To add one, retire one (`workflows/cap-and-retire.md`).

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
