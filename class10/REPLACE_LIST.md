# Class 10 update: what to replace

Copy the files below into `CBSE paper class 10/`, overwriting existing ones.

## Replace (existing files)
- chapters/cbse-2025-set2.tex
- chapters/cbse-2025-set2_formulae.tex
- codes/1.c, 10.c, 27.c, 32a.c, 34.c, 38.c
- codes/1plot.py
- figs/q1.png

## Add (new files)
- codes/11plot.py, 17plot.py, 21plot.py, 29plot.py, 38plot.py
- figs/q11.png, q17.png, q21b.png, q29.png, q38.png

## Delete (no longer used)
- codes/3.c, 9.c, 16.c, 16plot.py, 33.c  (removed questions)
- codes/a.out  (stray binary)
- figs/q1.tex, q11.tex, q17.tex, q29.tex, q38.tex  (replaced by PNGs plotted from coordinates)

## Question map (book number -> change)
| Book no. | CBSE Q | Change |
|---|---|---|
| 1.2.1 | Q1 | vector solution (tangent direction vectors), plot from points |
| 1.2.2 | Q3 | removed |
| 1.2.7 | Q9 | removed |
| 1.2.8 | Q10 | convolution + Z-transform |
| 1.2.11 | Q16 | removed |
| 1.2.14 | Q21(b) | plot of y = x^2 - 2x - 1 |
| 1.2.15, 1.2.16 | Q23 | removed |
| 1.2.17 | Q27 | convolution + Z-transform |
| 1.2.20 | Q32(a) | unit step function |
| 1.2.21 | Q33 | removed |
| 1.2.22 | Q34 | Gaussian elimination + rank |
| 1.2.24 | Q38 | vectors, plot from points |

Also redrawn from coordinates: Q11, Q17, Q29. After the removals the book has 18 problems (1.2.1 to 1.2.18).

Run each plot script from inside `codes/`, for example `python3 1plot.py`; it writes the PNG into `../figs/`.
