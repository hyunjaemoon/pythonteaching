# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A collection of Python teaching materials (inspired by UC Berkeley's CS61A) — lecture notes, homework problem sets, and a 2048 project. It is intentionally **solution-free**: `.py` files contain skeleton problems with `"*** YOUR CODE HERE ***"` placeholders that students fill in. Do NOT commit solutions to homework or lecture problems; the README explicitly forbids posting solutions to avoid academic dishonesty.

## Structure

- `src/lec1`–`src/lec8` — per-lecture PDFs plus a `codingpractice.py` skeleton for students to edit.
- `src/hw1`–`src/hw3` — homework skeletons (`hw01.py`, etc.) with doctest-style expected outputs in docstrings.
- `src/2048` — a tkinter 2048 game: `logic.py` is the student-implemented game logic (task-numbered skeleton functions with doctests), `puzzle.py` is the provided GUI that imports it.
- `src/practice` — extra practice problems with solution PDFs.

Plain Python 3.9+ standard library only (tkinter for 2048); no dependencies or test framework. `pyproject.toml` exists solely for ruff lint config — student skeleton directories (`src/hw*`, `src/lec*`) have lint largely disabled because unused placeholders are intentional.

## Common commands

- Verify a skeleton's doctests (once implemented): `python3 -m doctest src/hw1/hw01.py -v`
- Run the 2048 game: `cd src/2048 && python3 puzzle.py` (requires `logic.py` functions to be implemented)
