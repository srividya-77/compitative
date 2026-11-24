# compitative

A small collection of Python scripts for competitive programming practice.

## What it is

Three Python scripts solving basic problems:

- **`runner_up.py`** — reads a list of scores, removes the maximum, then prints the next highest value (the runner-up score)
- **`Runner_up.py`** — an earlier attempt at the same problem using `set()` and `sort()` to find the second unique highest score; contains a bug (`unique_scores` is referenced before it is assigned)
- **`leap_year.py`** — a function stub (`is_leap`) for determining whether a year is a leap year; the logic body is empty

## Built with

- Python 3

## How to run

```bash
cd compitative
python3 runner_up.py
```

Input format for the runner-up scripts: first line is the number of scores, second line is the scores separated by spaces.

Example:
```
5
2 3 6 6 5
```
Expected output: `5`
