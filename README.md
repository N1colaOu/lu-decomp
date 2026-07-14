# LU Decomposition Toolkit

This repository contains a small set of scripts created for a
university homework assignment: the goal is simply to implement LU
decomposition, observe the numerical errors that can arise, and compare
behaviour under different pivoting strategies. It's a pedagogical
project — intended to make the decomposition, its error characteristics,
and runtime hotspots easy to inspect.

What the files do

The repository is organised as a set of focused scripts and helpers:

- `lu_decomp.py` — the core LU factorisation implementation and
	supporting utilities.
- `comparison.py` — runs comparisons between different pivoting or
	algorithmic choices and reports results.
- `error.py` — computes residuals and numerical error metrics for the
	produced factorizations.
- `profiler_true.py` / `profiler_false.py` — simple profiling harnesses
	used to collect timing and line-level statistics with and without
	pivoting.
- `testing_d.py`, `testing_e.py`, `testing_f.py` — small test drivers
	and benchmarks used during development.
- `get_line_profiles.sh`, `view_line_profiles.sh` — shell helpers to
	extract and view line-level profiler output.

How to run and see the results

The scripts are plain Python (3.8+) and require no external packages to
run the basic examples. Typical commands you can run from the repo
root:

```bash
python3 lu_decomp.py         # run the core decomposition demo
python3 comparison.py       # compare strategies and print summary
python3 profiler_true.py    # collect profiling data (with pivoting)
python3 profiler_false.py   # collect profiling data (without pivoting)
./get_line_profiles.sh      # convert profiler output to line-level view
./view_line_profiles.sh     # open the line-level profile in a pager
```

Profiling outputs (JSON/text) are stored in the `build/` directory when
the profiler scripts are run — open those files to inspect timing and
hotspots, or run the shell helpers to generate a line-oriented view.
