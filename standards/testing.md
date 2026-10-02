# Testing

At most 15 rules. To add one, retire one (`workflows/cap-and-retire.md`).

- Tests use pytest.
- One test file per module.
- Use plain `assert`.
- Keep fixtures small.
- Every bug fix ships with a test that fails before the fix and passes after it.
- Do not mock the invoice maths. Test it for real.
- Tests must not touch the network.
- Tests must run in under 10 seconds in total.
- Name tests for the behaviour: `test_total_includes_tax`, not `test_1`.
