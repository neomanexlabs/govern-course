# Govern check

Run it after each count (`workflows/cap-and-retire.md`), and on any repo the team wants held to the same moves. Read only: change nothing.

For each item give PASS, FAIL or CAN'T TELL FROM THE REPO, with the evidence: a file and line, or a command and its output. A CAN'T TELL names the record that would settle it. Where the bug-fix steps live in an engine, read them there too.

1. **Root file.** `AGENTS.md` fits on one screen and states its word budget (`wc -w AGENTS.md`).
2. **Locked list.** The pull request template has a "Standards followed" list, locked before the work, and at least one review checked a change against it.
3. **Docs.** At least one doc, and a step that updates it when the code changes.
4. **Hook.** At least one hook, and a record of it tested both ways: blocked once, let through once.
5. **Bug-fix workflow.** In a file or an engine: a test that fails first, a reviewer who is not the fixer, a written result for each step, a failed review sent back to the red step. Where a skipped step is written down, and who reads it.
6. **Failure list.** Read first by the review, with a cap.
7. **Caps and the count.** A cap in every file that holds rules, the last count of how often each rule was cited, the fix-or-retire decision from it, and the reason written for every uncited rule kept (in `git log`, as step 6 of `workflows/cap-and-retire.md` records them).
8. **Loop edits.** Three edits the loops made (a class edit after a fix, a failure-list entry, a cap-and-retire change), each with its before and after (`git log -p`).

End with a table: item, verdict, evidence. The check finds; the team decides what to change.
