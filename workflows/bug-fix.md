# Bug fix

Every bug fix follows these steps, in order. Do not start a step before the one above it is done.

1. **Read.** Start the pull request description from `.github/pull_request_template.md` and fill in "Standards followed" (`AGENTS.md` says how).
2. **Red.** Add a test for the reported case to the test file of the code it covers (`tests/test_invoice.py` for `billing/invoice.py`). If the reported data is not in the repo, say so and say what you used instead. If a fix is already in the working tree, set it aside first (`git stash push billing/`). Run `python -m pytest -q` and see the new test fail on the wrong value, an assertion, not an error. Keep the failing line for the description.
3. **Fix.** Bring the fix back (`git stash pop`) or write it. Run `python -m pytest -q`: every test passes.
4. **Docs.** If the change makes a line in `docs/` wrong or incomplete, update it.
5. **Review.** Hand the change to the `reviewer` agent, with the "Standards followed" list. You wrote the fix, so you never review it yourself. On FAIL, fix each finding (a code finding goes back to step 2: a test that fails first, then the fix) and ask for a new review.
6. **Commit.** Only after the reviewer says PASS: code, tests and docs in one commit. Say in your reply what the review found.
