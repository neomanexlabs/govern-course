# Git and pull requests

## Git

- Branch from `main`.
- Branch names: `fix/<short-name>`, `feat/<short-name>`, `chore/<short-name>`.
- Commit messages: imperative mood, under 72 characters in the first line.
- Reference the invoice or ticket number when there is one.
- Do not force-push `main`.
- Rebase your branch on `main` before opening a pull request.
- Squash fixup commits before review.
- Tag releases `vYYYY.MM.DD`.

## Pull requests

- One change per pull request.
- Write what changed and why in the description.
- Add screenshots for anything visible in the web app.
- Link the ticket.
- Priya reviews money changes. Anyone can review the rest.
- Do not merge your own pull request unless it is a typo fix.
- If CI is red, do not merge.
- Keep pull requests under 400 lines where you can.
