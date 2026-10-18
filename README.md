# ADM – Homework 1

Homework 1 for **Algorithmic Methods of Data Mining** (M.Sc. in Data Science, Sapienza University of Rome), academic year 2026/2027.

The homework practises basic Python programming through challenges on [HackerRank](https://www.hackerrank.com).

## Repository contents

| Path | Description |
|------|-------------|
| `README.md` | This file: an overview of the repository. |
| `scripts.py` | The source code of every solved exercise, grouped by section. |
| `printouts/` | Screenshots and PDF printouts of the accepted submissions, from my HackerRank profile. |

## Exercises

### Problem 1 – Python challenges

| Section | Exercises |
|---------|-----------|
| Introduction | 7 |
| Basic Data Types | 6 |
| Strings | 14 |
| Sets | 13 |
| Collections | 8 |
| Date and Time | 2 |
| Exceptions | 1 |
| Built-ins | 3 (Zipped!, Athlete Sort, ginortS) |
| Python Functionals | 1 (Map and Lambda Function) |
| Regex and Parsing | 17 |
| XML | 2 |
| Closures and Decorators | 2 |
| Numpy | 15 |

### Problem 2 – Algorithms

| Exercise | Approach |
|----------|----------|
| Birthday Cake Candles | Count how many candles have the maximum height. |
| Number Line Jumps | Solve `x1 + j·v1 = x2 + j·v2`; the kangaroos meet when `j` is a non-negative integer. |
| Viral Advertising | Simulate day by day: `liked = shared // 2`, then `shared = liked · 3`. |
| Recursive Digit Sum | Compute `digit_sum(n) · k` instead of building the repeated string, then reduce to one digit. |
| Insertion Sort – Part 1 | Shift larger elements right, printing after each shift, then insert. |
| Insertion Sort – Part 2 | Full insertion sort, printing the array after each pass. |

## Notes

- Every section of `scripts.py` is a separate HackerRank submission that reads from standard input. Run each one on its own, not the whole file at once.
- All solutions use **Python 3**, except *Tuples*, which was submitted with **PyPy 3**. The expected output on HackerRank comes from PyPy's tuple hash.
- *Exceptions*: newer Python 3 versions word the `ZeroDivisionError` message differently, so the solution prints the message HackerRank expects explicitly.
- **AI assistance:** I wrote these solutions with the help of an AI assistant (Claude) due to time constraint, as the homework instructions require me to disclose.

## Author

<!-- Abel Asefa -->
