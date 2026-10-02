# Failures the review missed

The reviewer reads this list first and checks every change for each entry. An entry is a mistake that reached `main` after a review passed it: what to check, and one line of where it came from.

At most 10 entries. When the list is full, retire one before you add one (`workflows/cap-and-retire.md`).

- **A doc written as history.** A doc says what is true now. When a known issue is fixed, its line goes. A line that says something was fixed, or when, is history: Git keeps it. (Missed: both reviews of the INV-2040 fix passed "None open … is fixed".)
