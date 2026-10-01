# Govern Course Workspace: Acme Billing

The practice repo for Neomanex's Govern course, a course for engineering teams whose developers each run an AI coding agent (Claude Code, Cursor, Codex, Copilot, OpenCode). It is a small, fictional invoicing app kept by a six-person team. Every lesson makes one change to how the team's agents work, and each lesson's result is a git tag, so you can start any lesson from the one before it and compare your work with ours.

The lessons are on Neomanex Learn: https://neomanex.com/learn

```bash
git clone https://github.com/neomanexlabs/govern-course.git
cd govern-course
git checkout l0
python -m pytest -q
```

## Tags

| Tag | The repo after |
|---|---|
| `l0` | the start: one long shared `AGENTS.md` (19 sections, 1,315 words), no standards |
| `l1` | lesson 1: a short `AGENTS.md` (142 words) with the rules every change must follow and a table of what to read, `CLAUDE.md` importing it, the rest moved to `standards/` and `docs/` |
| `l2` | lesson 2: a pull request template (`.github/pull_request_template.md`) whose "Standards followed" list is written before any code and then locked, and one rule in `AGENTS.md` (167 words) to start every change from it; the review checks each change against that list |

To do a lesson, check out the tag before it on a branch of your own (`git checkout -b my-l1 l0`), make the change, then compare: `git diff l1`.

## What is in it

| Path | What |
|---|---|
| `billing/invoice.py` | invoices, lines, subtotal, tax, total |
| `tests/` | the pytest suite |
| `AGENTS.md` | the team's instructions for AI agents |

It carries one known bug on purpose: invoice INV-2040 shows the wrong total. The lessons use it as the job the agents are asked to do.

Needs Python 3.12 and pytest.

## About Neomanex

Neomanex is an AI-native company. We run our own business on an AI Operating Model,
publish the evidence, and help other companies become AI native: agents, operations,
and the infrastructure underneath them, built and governed in production.

This project is part of that work.

- Website: https://neomanex.com
- Work with us: https://neomanex.com/contact
- Products: [ConvOps](https://convops.app) (AI-first operations) and [Gnosari](https://gnosari.com) (conversational data collection: AI agents that turn conversations into structured data)
