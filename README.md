# The Zero → Software Engineer Study Plan

A 7-phase, project-driven curriculum for going from absolute beginner to a working software engineer.

**Assumptions baked into this plan**
- You have never programmed (or barely have).
- You do not have a CS degree.
- You have a Mac (this machine is `darwin`, arm64) but will deploy to Linux.
- Python 3.13 is your tool for most phases.
- ~2 to 3 hours/day, 6 days/week. Adjust the schedule, keep the order.

**Ground rules that make this work**
1. **Typing is not reading.** You do not understand a topic until you have written code that breaks.
2. **Every phase ends with a project.** Not a tutorial. Not a video. A thing you built.
3. **Phase 1 math is not optional.** It is the single highest-leverage phase. Skip it and everything after becomes cargo cult.
4. **No "I'll learn it later."** If a concept doesn't make sense, it goes on a `BLOCKERS.md` list and you resolve it within 48h.
5. **You may not advance to phase N+1 until phase N's exit gate is passed.** The gates are at the bottom of each phase.

---

## Table of Contents

- [Phase Overview](#phase-overview)
- [Phase 0 - Environment & Tooling](#phase-0--environment--tooling)
- [Phase 1 - Math Foundations (30 warm-up + 150 programs)](#phase-1--math-foundations-30-warm-up--150-programs)
- [Phase 2 - Python + OOP](#phase-2--python--oop)
- [Phase 3 - Linux & the Terminal](#phase-3--linux--the-terminal)
- [Phase 4 - OS, Processes, Databases, Networking (practical)](#phase-4--os-processes-databases-networking-practical)
- [Phase 5 - The Web, End to End + FastAPI](#phase-5--the-web-end-to-end--fastapi)
- [Phase 6 - Containers, Deployment, Pipelines](#phase-6--containers-deployment-pipelines)
- [Phase 7 - System Design](#phase-7--system-design)
- [Appendices](#appendices)

---

## Phase Overview

| Phase | Focus | Duration | Exit deliverable |
|---|---|---|---|
| 0 | Environment & toolchain | 1–2 days | Python + Git + editor working |
| 1 | Math, beginner → advanced (all as programs) | 8–10 weeks | 30 warm-up + 150 programs written |
| 2 | Python + OOP + projects | 14–16 weeks | 3-tier project portfolio (24 projects, 213 requirements) |
| 3 | Linux & terminal, debugging-first | 3–4 weeks | Debugging playbook working |
| 4 | OS, processes, DB, networking | 10–12 weeks | Systems project w/ logs |
| 5 | Web fundamentals + FastAPI | 8–10 weeks | Full-stack API + HTTP trace writeup |
| 6 | Docker, deploy, CI/CD | 6–8 weeks | Live URL from a push |
| 7 | System design | ongoing | 10 design docs + flagship project |

**Total: ~12 months at 2–3h/day.** That is normal and honest.

---

## Phase 0 - Environment & Tooling

> Half a day. Do not skip. Broken tooling kills momentum.

### Setup checklist
- [ ] Install Python 3.12+ (`python3 --version`)
- [ ] Create a virtual environment and understand *why* (Phase 4 explains the mechanics)
- [ ] Install `git`, configure `user.name` / `user.email`
- [ ] Pick an editor. VS Code is fine. Learn: multi-cursor, goto-definition, rename symbol, integrated terminal.
- [ ] Learn to run from the terminal, not just click "Run"
- [ ] Get a free Linux box for practice:
  - [Oracle Cloud Always Free](https://www.oracle.com/cloud/free/) (real VM, best)
  - [Google Cloud Shell](https://shell.cloud.google.com) (zero setup)
  - [GitHub Codespaces](https://github.com/codespaces) (60h/month free for personal accounts)
- [ ] Commit every day and keep each phase in its own folder inside the repo

### Repository layout
This repo is the working directory itself. It is the codebase you will push to GitHub and share with your partner.

Keep the repo organized by phase, and inside each phase keep each task, project, or problem in its own folder.

```text
repo-root/
├── phase0/
│   ├── setup/
│   ├── notes/
│   └── checklists/
├── phase1/
│   ├── warmup/
│   │   ├── t001_hello_world.py
│   │   ├── t002_add_two_numbers.py
│   │   └── ...
│   └── problems/
│       ├── level0/
│       │   ├── p001_order_of_operations.py
│       │   └── ...
│       └── level1/
├── phase2/
│   ├── oop/
│   ├── projects/
│   │   ├── project_01_cli_app/
│   │   ├── project_02_bank_account/
│   │   └── ...
│   └── notes/
├── phase3/
│   ├── shell_practice/
│   ├── debugging_playbook/
│   └── projects/
├── phase4/
│   ├── systems/
│   ├── db/
│   └── projects/
├── phase5/
│   ├── api_projects/
│   └── fastapi_apps/
├── phase6/
│   ├── docker/
│   ├── deploy/
│   └── ci_cd/
├── phase7/
│   ├── design_docs/
│   └── flagship_project/
├── README.md
├── AGENTS.md
├── .gitignore
└── .github/
```

Use a consistent naming pattern:
- `phaseN/` for each phase
- `warmup/`, `problems/`, `projects/`, `notes/`, `apps/`, or `docs/` inside each phase
- `t001_...py`, `p001_...py`, or `project_01_.../` for individual work units

### The habit that starts now
```bash
cd /path/to/your/project

git init
git branch -M main
git add .
git commit -m "day 0: it begins"
git remote add origin git@github.com:YOUR_USER/YOUR_REPO.git
git push -u origin main
```

If you want to keep the repo collaborative, each person clones the same GitHub repo and works in the same folder structure. The important part is that the repo lives where you are working now, not in a different directory like `~/dev/study`.

### You must be able to answer these
1. What is the difference between a file and a folder on your OS?
2. What is `PATH`, and how does the shell find `python3`?
3. What does a **virtual environment** actually contain, and why does it exist?
4. What does `git` track? What does it *not* track?

**Exit gate:** you can open a terminal in any directory, activate a venv, run a script, and commit it.

---

## Phase 1 - Math Foundations (30 warm-up + 150 programs)

> **Why this phase exists.** Every hard thing in software is math wearing a disguise: load balancing is weighted averages, rate limiting is probability, hashing is modular arithmetic, system design is cost analysis under constraints, rendering is linear algebra. This phase is not academic - it is removing the ceiling that will otherwise hit you in Phase 7.

**Everything here is a program you write, not an exercise you solve.** Even "solve `3x + 7 = 22`" means *"write a program whose input is `3, 7, 22` and whose output is `5`, without calling `sympy`."* The moment you can only do the math in your head, you've learned nothing for this career.

**Every row in the 150 has a "Where it's actually used" column. Do not skip it.**

That column is the entire point of the phase. Dot products with no context are trivia you'll forget by Phase 7; "the dot product *is* cosine similarity, which *is* how every vector search and RAG retriever scores relevance" is a fact you'll use while designing a search system.

For each problem, your commit must include one line answering: **"Where have I seen this before?"** A concrete prior — a real bug, a real library, a real feature — not a vague one. If you can't name one, you haven't looked hard enough, and that's a signal to go read the source of something that uses it.

**Method — do it wrong and you'll waste 10 weeks:**
1. **Read the prompt. Close the file.** Say out loud what the program must do, in plain English.
2. **Write it in Python.** `phase1/warmup/t004_add_two_numbers.py`. Run it. Break it on purpose.
3. **Print every intermediate value.** If the math is invisible in the output, you don't understand it yet.
4. **Write a 3-line docstring:** what it does, what it takes, what it returns.
5. **Add an assertion or two.** If `7 // 2` is involved, you should be testing it.
6. **Name the real-world use** from the last column, and where you've seen it. Put it at the top of the file as a comment.
7. **Commit.** Daily. `git commit -m "phase1: T004 add two numbers"`
8. **Stuck for 20 minutes?** Look at the *hint* only, not a full solution. Then close it and re-derive.
9. **Re-solve it cold 3 days later.** From memory, in a new file.

**Hard rule:** you may not use a library that solves the thing for you. No `math.gcd` in problem 3, no `sympy.solve` in problem 21, no `numpy.linalg.eigvals` in problem 138. Implement it yourself once. *Then* compare against the library and understand why they agree.

---

### Phase 1A - Programming Warm-Up (T1–T30)

> **If any of these feel hard, do not start Phase 1 yet.** These are the "multiply two numbers" tier. They exist because "math foundations" for most people means "I want to skip the math foundations."
>
> These are not jokes. Reverse a string and you'll use the same index logic when parsing logs. FizzBuzz teaches modulo and branching. Converting seconds to hours is literally what every duration/timestamp formatter does.

Every task below maps to something you'll actually build in Phases 2–7.

| # | Task | Why you need it |
|---|---|---|
| T1 | Print `Hello, World!` | Sanity check that your toolchain runs at all |
| T2 | Add two numbers. Hardcode `a` and `b`, then again taking them from `input()` | Every function you'll ever write starts here. Also your first `input()` — which always surprises people |
| T3 | Subtract two numbers | Same shape as T2. This is the point: the shape is what matters, not the operation |
| T4 | Multiply two numbers | Same again. By T4 you should stop needing to think about it |
| T5 | Divide two numbers. Print what happens when the divisor is `0`, and handle it | **First error handling.** `ZeroDivisionError` → the first defensive-programming instinct you'll need forever |
| T6 | Take two numbers and print `/`, `//`, `%`, `**` results for both, side by side | The four operators that differ between Python and most other languages. Bit me constantly |
| T7 | Find the remainder of `17 % 5`. Then: "is 17 odd or even?" using only `%` | **Cron scheduling and sharding.** `user_id % 8` decides which server gets the user |
| T8 | Swap two variables. Once with a temp, once without | Python's multiple-assignment trick. You'll see `a, b = b, a` everywhere |
| T9 | Take a 3-digit number and print its digits separately: `409` → `4 0 9` | String indexing + integer division. This is how you parse a raw log line or a fixed-width protocol field |
| T10 | Reverse a 3-digit number. `409` → `904` | String slicing `[::-1]`. Foundation of every reverse, paginate, and parse operation |
| T11 | Check if a number is positive, negative, or zero | `if/elif/else`. **Every** conditional logic you'll ever write starts here |
| T12 | Given 2 numbers, print the larger. Then all 3 of larger / smaller / equal | Comparison operators. Validation branches in every API handler |
| T13 | Given 3 numbers, print the largest. Try to do it without `max()` | Nested conditionals. Learning to see *how* a builtin is implemented |
| T14 | Given a year, print whether it's a leap year | Boolean logic with `and`/`or`/`not`. Rule engines look exactly like this |
| T15 | Sum the digits of `4825`. Then find the digit product | The **divmod** pattern. Used for currency conversion, base conversion, and unit splitting |
| T16 | Factorial of `n`. Handle `0!`. Then loop for `n=10` | The classic "learn loops" exercise. Edge case `0!` teaches you to think about boundaries |
| T17 | Print the multiplication table of `7` from 1 to 10 | A single loop with a counter. For a nested-loop extension, print the tables for 1 through 10, each from ×1 to ×10 |
| T18 | Print the first 100 numbers. Then only the evens. Then only the multiples of 7 | `range()` with steps. This is how paginate, batch, and rate-limit windows work |
| T19 | Print the first 10 Fibonacci numbers, iteratively | Recurrence in code. This is your first "state" variable — the core of OOP later |
| T20 | Sum `1` to `n`. Then sum the evens, then the odds | Accumulator pattern. **Every** aggregation, sum, and fold in data processing is this |
| T21 | Average of a hardcoded list. Then the median of the same list | `sum()`/`len()`, then sorting. Mean vs median is the p99-vs-average argument in miniature |
| T22 | Max and min of a list — without `max()`/`min()` | Iterating a collection. Slash counts, longest word, hottest day |
| T23 | Reverse a **string** (`"python"` → `"nohtyp"`) | Strings as sequences. You'll slice strings constantly in parsing and formatting |
| T24 | Check if a string is a palindrome (`"racecar"`) | String slicing + conditionals. Also: input validation in production forms |
| T25 | Count vowels in a sentence. Then count each letter's frequency | **The `dict` frequency pattern.** This is log analysis, word counts, and metrics aggregation |
| T26 | Convert Celsius to Fahrenheit, and Fahrenheit to Celsius | Formula-following. The template for every unit conversion in a data pipeline |
| T27 | Convert inches to centimeters, and cm to feet+inches | Compound division with remainder. Multi-unit conversion in real systems |
| T28 | Given seconds, print `H hours M minutes S seconds` for `9000` | **Duration formatting.** Uptime displays, log timestamps, rate-limit windows, SLA countdowns |
| T29 | Ask for length and width; print the rectangle's area and perimeter | Formulas + `input()`. Interaction pattern for every CLI tool |
| T30 | Make a tiny unit converter: prompt for a value, ask which direction, print the result | Your first real program: input, branching, formatting, output |

**Warm-up exit gate:** T1–T30 all committed and running. T16, T19, T24, T28 re-written cold from memory. You can open a blank file and write a loop with a counter without hesitating.

---

### Phase 1B - The 150

### Level 0 - Number sense & arithmetic (Problems 1–20)

Foundations you'll never stop using.

| # | Task | Skill | Where it's actually used |
|---|---|---|---|
| 1 | Write a program that prints `2 + 3 * 4` and `-2 ** 2`. Then explain, in a comment, why the two "4"s disagree. | Order of operations | Precedence bugs in SQL, YAML, and shell `$(( ))` — why every language documents it first |
| 2 | Write a program that takes `a=7, b=2` and prints `a/b`, `a//b`, `a%b` as a labelled table. Explain what `%` is *for*. | Python int/float division | `%` = cron schedules, keysharding (`user_id % 16`), even/odd routing, pagination remainders |
| 3 | Write `gcd(a, b)` using a loop and Euclid's algorithm. **Do not** call `math.gcd`. Test with `(48, 18)` and print every iteration. | GCD | Scheduling non-overlapping intervals, reducing image aspect ratios, finding common divisors of chunk sizes |
| 4 | Write `lcm(a, b)` from scratch. Then write a brute-force checker that loops 1→`a*b` and compare the two for 50 random pairs. | LCM | Merging two periodic schedules (cron + retry timer), aligning batch windows, sync cadences |
| 5 | Write `divisors(n)` returning every divisor of `24`. Then run it on `360`. | Divisors | Index-space planning: how many buckets can evenly split N items. Also file permissions (`chmod 755` = 4+2+1 divisors) |
| 6 | Write `factorize(n)` that returns the prime factorization of `360` as a `{prime: power}` dict. | Factorization | Dependency resolution, factoring large numbers (crypto), optimizing schedules by prime-factor grouping |
| 7 | Write `is_prime(n)` with a loop. Use it to prove `7919` is prime by printing every number you tested. | Primality | Generating prime-sized hash buckets, RSA key sizes, deciding timeout backoff factors |
| 8 | Write a program that prints `round(2.675, 2)`, `format(2.675, '.2f')`, and the `Decimal` version. Explain in a docstring why they disagree. | Float representation | **Money.** Every billing system, currency conversion, and float comparison bug in production |
| 9 | For `a=-7, b=3`, print `a/b`, `a//b`, `math.floor`, `math.ceil`, and `int(a/b)` side by side. Label which is which. | Rounding families | Truncating vs rounding in pagination, downsampling metrics, expiring rate-limit windows |
| 10 | Write `percent_change(old, new)` and apply it to 40 → 50. | Percent change | CPU/memory growth deltas, latency regression %, "error rate went up 300%" |
| 11 | Apply your function to 50 → 40. Add one comment line explaining the asymmetry. | Percent change | Alerting: -50% and +50% are the same magnitude but read completely differently to a human on call |
| 12 | Write `simple_interest(principal, rate, years)`. Run `$2000 @ 5% for 3 years`. | Simple interest | Credit/loan calculators, AWS's *simple* monthly billing vs Azure's tiered one |
| 13 | Write a loop computing compound interest on `$2000 @ 5% compounded monthly for 3 years`. Print the balance every year, and the final number. | Compound interest | Accruing debt/interest, growth projections in planning docs, APY vs nominal rate |
| 14 | Write `scale_ratio(a, b, total)` that splits `64` in the ratio `3:5`. Handle ratios that don't divide evenly. | Ratio & proportion | Splitting traffic 3:5 across regions, weighted round-robin, mixing test/prod config |
| 15 | Write four functions — `km_to_m`, `m_to_cm`, `cm_to_mm` — and chain them to convert `42.195 km` all the way to millimetres. | Unit conversion | Real-time systems: 42.195 km is a marathon. SI vs imperial in game/physics engines |
| 16 | Write `seconds_to_parts(seconds)` that breaks `9000` into h/m/s. Add a long comment about leap seconds and why we ignore them. | Time arithmetic | Formatting any duration: "uptime 14d 3h 22m", log timestamps, rate-limit windows |
| 17 | Write `roman_to_int("MCMLXXXIV")` and `int_to_roman(1984)` using lookup tables. Round-trip test them. | Roman numerals | **Excel column letters** (A, B… AA) are a bijective base-26 — same shape of math |
| 18 | Write `to_base(n, base)` and `from_base(s, base)` for base 2 and 16. Convert `255` both ways and assert round-trip equality. | Bases | Hex color codes `#RRGGBB`, memory addresses in a debugger, `0x` and `0b` literals in config |
| 19 | Convert `0b1011` to decimal and to hex. Then do the binary conversion **again using only bit shifts and masks**. Compare results. | Binary | Every bitmap, permission bitfield, flag enum, and network packet you ever parse |
| 20 | Write `to_scientific(n)` that rewrites `0.0000042` in scientific notation, and `sig_figs(n)` that counts significant figures. | Scientific notation | Latency magnitudes (p99 = 1.4e-4 s), scientific data, avoiding float overflow |

**Sanity check before moving on:** write a program that explains *why* `0.1 + 0.2 != 0.3` at the binary level. If you can't, revisit T6 and #8.

---

### Level 1 - Algebra & equations (Problems 21–40)

The language every error message and every formula is written in.

| # | Problem | Skill |
|---|---|---|
| 21 | Write `solve_linear(a, b, c)` solving `ax + b = c`, printing every algebraic step. Solve `3x + 7 = 22`. | Linear equation | Turning a rate + target into an action: "at 3 errors/min, how long until 22?" — SLO burn math |
| 22 | Generalize to `(ax - b) / c = d`. Solve `(2x - 3) / 5 = 7`. | Multi-step equation | Unwinding a nested config or expression, e.g. parsing a query string back to a raw value |
| 23 | Write a solver for `a(bx + c) = d`. Solve `2(x + 3) = 5x - 9`. | Distribution | Isolating a variable buried in nested function calls: `solve_for_concurrency(rps, workers, latency)` |
| 24 | Write `solve_2x2()` for two simultaneous equations using substitution. Solve `x + y = 10`, `x - y = 4`, and print the ordered pair. | 2×2 system | Two servers, two constraints: split load and hit a latency target simultaneously |
| 25 | Reuse your solver for `2x + 3y = 12`, `x - y = 1`. | 2×2 system | Sizing CPU vs memory so cost stays under budget — the classic system-design constraint pair |
| 26 | Extend it to detect and explain the three cases: unique solution, no solution, infinite solutions. Construct all three. | Parallel lines | Over-constrained autoscale rules that **can never fire** — a real prod bug class |
| 27 | Write `roots_by_factoring(a, b, c)` that searches for integer factors. Solve `x² - 5x + 6 = 0`. | Quadratic | Where does a quadratic model beat a linear one? Any A/B test curve, any S-curve adoption forecast |
| 28 | Write `quadratic_formula(a, b, c)`. Solve `3x² - 5x - 2 = 0`. Cross-check against #27. | Quadratic formula | Fitting a latency-vs-concurrency curve to find the knee where you *must* add a server |
| 29 | Write `complete_the_square(a, b, c)` returning `(h, k)` for the vertex. Solve `x² - 6x + 5 = 0`. | Completing square | Finding the *optimal* point — cheapest config, best batch size, minimum-cost threshold |
| 30 | Write `discriminant(a,b,c)` and `describe_roots()` printing "two real / one real / no real". Apply to `2x² + 3x - 2 = 0`. | Discriminant | Checking whether a model is even solvable before you deploy logic based on it |
| 31 | Write `solve_shop_prices(...)` for: 3 pens cost the same as 2 pencils, pens are $1.40 more. Print both prices. | Word problem | Every pricing tier / discount ladder you ever build |
| 32 | Write `solve_age_problem(...)`: a father is 4× his son's age; in 6 years he'll be 3×. Print both ages now and in 6 years. | Age problem | **Schema versioning** — v1 has 3× the rows, converging to 1× at migration time. Same math. |
| 33 | Write `solve_mixture(v1, p1, v2, p2, target_p)`. Mix 20% acid into pure acid to reach 50%. | Mixture | **Read replica lag**: old% + new% mixed = target%. Traffic splitting ratios live here |
| 34 | Write `time_to_fill(tank_times)` that combines pipe rates (loop over a 1-hour slice, and also solve it algebraically — compare). | Work rate | Parallel workers, parallel replicas, parallel API calls — do rates actually add? |
| 35 | Write `average_speed(distances, speeds)` that returns the correct average. Test with 60km@40km/h then 40km@80km/h. Prove it's not 60. | Average speed | **The #1 interview trap.** Also: you cannot average latencies across differently-sized batches |
| 36 | Write `solve_inequality(a, b, c)` for `ax + b < c`, returning a string interval like `"(3.5, inf)"`. | Inequality | Every alert threshold and every `assert` in a test suite is an inequality |
| 37 | Write `solve_abs_equation(a, b, c)` for `\|ax + b\| = c`. Then extend it to `> c`. Solve both given cases. | Absolute value | Distance from a target, jitter windows, "within 5% of expected" tolerance checks |
| 38 | Write `simplify_exponents(terms)` that combines like bases: `x² · x³ · x⁻² / x⁴`. | Exponent laws | The repeated-squaring identity in RSA, and every exponentiation micro-optimization |
| 39 | Write `solve_exp(base, target)` that finds `x` for `2^x = 32`, `3^x = 81`, `4^x = 0.25` by searching, not by `math.log`. | Exponent equations | "How many doublings until this fills up?" — capacity planning in one line |
| 40 | Write `simplify_radical(n)` returning `(a, b)` for `√n = a√b`. Verify in Python. | Radical simplification | Standard deviation is a square root. So is RMSE. So is every norm-based distance. |

**Sanity check:** make #35 a small program that asserts the naive answer (60) is wrong and prints why.

---

### Level 2 - Functions, graphs, exponents & logs (Problems 41–60)

This is where you learn to read a graph - essential for debugging dashboards, latency plots, and UIs.

| # | Problem | Skill |
|---|---|---|
| 41 | Write `is_function(relation)` that runs the vertical line test on a list of points. Use it on `y² = x` (generate the points) and `x² = y`. | Function test | Understanding why `dict` keys must be unique but `list` items needn't be — one-to-one vs many-to-one |
| 42 | Write `evaluate_table(table, x)` and `find_inverse_table(table, y)` over a dict you define by hand. | Function eval | Lookup tables: HTTP status codes, error-code mappings, currency tables, feature-flag → config maps |
| 43 | Write `domain_of(f)` for `1/(x-3)` that prints the excluded value. Then draw the curve with `matplotlib`. | Domain/range | `ZeroDivisionError`, `NULL` semantics, validation: what inputs are *legal* for this function? |
| 44 | Write `compose(f, g, x)` and evaluate `f(g(2))` and `g(f(2))` for `f(x)=x²+1`, `g(x)=x-3`. | Composition | Function chaining, decorators, middleware pipelines, `then`/promise chains |
| 45 | Write `inverse_linear(a, b)` for `f(x) = ax + b`, verify by composing `f` with its inverse at 5 points. | Inverse | Encode/decode, encrypt/decrypt, serialization round-trips, reversible migrations |
| 46 | Write `slope(p1, p2)`. Use it on (2,3) and (7,11). | Slope | **Rate of change.** Requests/sec, bytes/sec, error-rate graphs, "how fast is this growing?" |
| 47 | Write `line_through(p1, p2)` returning the equation `y = mx + c` as a string. Use it on (0,4) and (3,10). | Line equations | Linear regression for trend lines, forecasting capacity from a plot, `y = mx + c` scoring models |
| 48 | Write `relation(m1, m2)` returning `"parallel"`, `"perpendicular"`, or `"neither"`. Test slopes 2 and ½. | Line relations | Orthogonality in vector spaces, dot-product = 0 checks, independent feature axes in ML |
| 49 | Write `midpoint(p1, p2)`. Verify the midpoint is equidistant from both points. | Midpoint | Grid snapping, halving a range to find a pivot, load-balancing between two backends |
| 50 | Write `distance(p1, p2)`. Assert it's 5 for (0,0)–(3,4) and 10 for (1,2)–(7,10). | Distance formula | Euclidean distance: vector search, nearest-neighbor, k-means, "find the closest server", spatial indexes |
| 51 | Write `vertex(a, b, c)` and use it on `y = x² - 6x + 5`. Plot the parabola and mark the vertex. | Vertex form | Finding the optimum — best batch size, minimum-cost threshold, the knee of a latency curve |
| 52 | Write a program that generates and plots all 3 discriminant cases (2 roots, 1 root, 0 roots). | Quadratic graphs | Seeing where a model has no valid solution before you trust it |
| 53 | Write `years_to_double(balance, target)` simulating growth year by year. $1000 → $100,000. | Exponential growth | Runaway growth: viral load, cache stampede, retry storms, "is this queue going to melt down?" |
| 54 | Write `solve_log(base, target)` that finds `x` for `log₂(x)=5` and `log₅(x)=2` by searching. | Log definition | Logs are the *inverse* of exponential growth — the tool for "how long until it doubles?" |
| 55 | Write `log_any(base, x)` using change of base. Compute `log₂(100)` and `log₇(50)`. | Change of base | Why `O(log n)` beats `O(n)`: binary search depth, and log-scale plots for 10⁰→10⁹ |
| 56 | Write `decay_model(sample, half_life)`. Print the value at `t = half_life` and assert it's half. | Exponential decay | Cache TTLs, token expiry, cooldown/backoff windows, engagement decay, memory leak modeling |
| 57 | Write `solve_continuous(p, r, target)` for `$5000 @ 7% compounded continuously`. Solve for `t`. | Log in the wild | Continuous integration, smooth-rate modeling, "how long until the queue drains?" |
| 58 | Write `piecewise_eval(f, x)` over a list of `(condition, value)` branches. Evaluate at 3 points and find the discontinuity. | Piecewise | **Tiered anything**: free tier vs paid, rate limits by key type, pagination by page size |
| 59 | Write `classify_model(story)` — a program that reads a scenario from the user and picks linear / exponential / quadratic, with a reason. | Model selection | Choosing an algorithm for real data. Right model = accurate prediction; wrong model = silent nonsense |
| 60 | Write `transform(f, kind)` generating `f(x)+3`, `2f(x)`, `f(-x)`, `f(x-2)`. Plot all four on one figure. | Graph transforms | Image transforms (brightness/scale/flip), CNN augmentation, CSS transforms, game coordinates |

---

### Level 3 - Geometry & trigonometry (Problems 61–78)

Geometry powers spatial reasoning (rendering, layouts, collision detection). Trig powers anything periodic (signal handling, animation, audio, game loops).

| # | Problem | Skill |
|---|---|---|
| 61 | Write `hypotenuse(a, b)`. Compute it for legs 9 and 12. | Pythagorean | Euclidean distance, vector magnitude, game physics, "how far apart are these two points?" |
| 62 | Write `coord_distance(p1, p2)` — your own `math.dist` from scratch. Test both given pairs. | Coordinate distance | Geo-fencing, nearest replica selection, map apps, routing |
| 63 | Write `shoelace(points)` for any polygon. Compute a triangle's area from 3 coordinates, then verify by splitting it into two triangles. | Shoelace | **Collision detection** in games, land/zone area calc, computer vision masks, concave-hull checks |
| 64 | Write `circle_props(r)` → circumference, area, and the arc length for a 90° sweep. Use `r=7`. | Circle & arc | Progress rings in UIs, dial gauges, geospatial radii, circular buffers |
| 65 | Write `sector_area(r, degrees)`. Compute the area of a 45° sector of `r=7`. | Sector | Pie charts, wedge allocation in storage, radar sweeps |
| 66 | Write `cylinder(r, h)` → volume and surface area. Include the two caps. Use `r=3, h=10`. | Cylinder | Cylinders *are* the canonical database problem: volume ≈ capacity, surface ≈ I/O cost |
| 67 | Write `cone(r, h)`, `sphere(r)`, `hemisphere(r)`. Volume + surface area for each. | Solids of revolution | Blob storage, ballistics, spherical shells, geometry kernels, ray-tracing primitives |
| 68 | Write `pyramid(base_area, h)` and `triangular_prism(base, h, length)`. | Volume formulas | 3D asset sizing, storage pyramids, composite shapes |
| 69 | Write `trapezoid_area(b1, b2, h)` and `parallelogram_area(b, h)`. Use bases 8 and 14, height 5. | Polygon area | Rule of 72 for doubling time, trapezoidal integration for area-under-curve metrics |
| 70 | Write `solve_angle_relation(ratio)` for complementary/supplementary pairs. One angle is 3× the other; find both. | Angle relations | CSS `transform: rotate(45deg)`, camera angles, sprite rotation, crypto key angle diagrams |
| 71 | Write `third_angle(a, b)` and put a thorough explanation of *why* triangle angles sum to 180° in the docstring. | Triangle angles | Mesh geometry, constraint validation, why ray-triangle intersection tests work |
| 72 | Write `classify_triangle(a, b, c)` returning the type. Add an assertion proving a triangle can't have two right angles. | Triangle types | Triangle inequalities in mesh collision, constraint solving, detecting degenerate data |
| 73 | Write `trig_from_sin_ratio(sin)` — given `sin θ = 3/5`, return the missing side and all of sin/cos/tan. | SOH-CAH-TOA | Game movement (velocity components), camera projection, wave sampling |
| 74 | Write `inverse_trig('cos', 0.6)` returning θ in both degrees and radians. | Inverse trig | Converting a similarity score or angle back into a raw value |
| 75 | Write `law_of_cosines(a, b, c)` for the largest angle. Use sides 7, 8, 9. | Law of cosines | 3D distance when you only have 2 of 3 coords — GPS, feature vectors, geometry engines |
| 76 | Write a program that prints a lookup table of exact sin/cos/tan for 30°, 45°, 60° and asserts them. | Special angles | Fast approximations in graphics; unit tests that must match exactly |
| 77 | Write `unit_circle(degrees)` returning `(x, y)`. Compute for 210°, 300°, 135°. | Unit circle | Trig functions all live here — this is the table behind `math.sin` |
| 78 | Write `to_radians(deg)` and `arc_length(r, radians)`. Convert 180° → π, then arc length for `r=10, θ=3π/4`. | Radians | **Why libraries store angles in radians**: smooth interpolation, rotation without drift |

---

### Level 4 - Counting, probability & statistics (Problems 79–98)

**This level is directly load-bearing for engineering.** Probability = retries, hashing, sampling, load distribution, A/B tests, queue sizing, error rates.

| # | Problem | Skill |
|---|---|---|
| 79 | Write `count_passwords(length, alphabet)` returning the number of 6-letter passwords from 26 letters. | Counting rule | Password-space security: how long must a secret be to resist brute force? |
| 80 | Write `factorial(n)` and `permutation(n, r)` from scratch. Compare `5!` against `P(5,2)`. | Permutations | Number of possible **orderings** — test-case permutations, exhaustive path enumeration, `itertools.permutations` |
| 81 | Write `combination(n, r)` by building Pascal's triangle. Then compare against `math.comb` for every `n` up to 20. | Combinations | Choosing subsets: which test cases to run, which servers to deploy to, feature-selection combos |
| 82 | Write `coin_outcomes(flips)` that enumerates all outcomes of 2 coins × 10 flips and counts HH. | Sample space | Enumerating all states to guarantee you've covered them — exhaustive testing, state machines |
| 83 | Write `dice_sum_distribution()` producing all 36 outcomes, then plot the sums as a bar chart. | Distributions | Load distribution: are requests uniform, normal, or Zipf? Sharding skew detection |
| 84 | Write `p_at_least_one_six(rolls)` using the complement rule, then verify with brute-force enumeration. | Complement rule | **"Probability at least one failure occurs"** — the retry/DLQ calculation. Also SQL `NOT EXISTS` anti-join patterns |
| 85 | Write `p_sum_seven()` that enumerates all 36 outcomes. Print them all — don't just count. | Enumeration | Brute-force verification: cheap to enumerate, impossible to reason about |
| 86 | Write `birthday_collision(n_people)`; find where P crosses 50%, then simulate it 1000 times. | Birthday paradox | **Hash collisions.** Why a 32-bit ID collides at ~77k items. Why MD5 is dead for integrity |
| 87 | Write `conditional_prob()` for a 3-red/5-blue bag, drawing 2 without replacement. Verify by simulation. | Conditional prob | Pinned-version dependencies, conditional feature access, correlated failures |
| 88 | Write `bayes(prevalence, sensitivity, specificity)`. Use it for the disease-test problem and show why the answer is ~16%, not 99%. | Bayes' theorem | Anomaly detection, alert triage, spam filtering — inverting a test's accuracy given base rates |
| 89 | Write `expected_value(outcomes)` for the dice game, then simulate 100,000 games. Would you play? | Expected value | Expected latency, expected cost per request, expected retries — and whether an optimization pays for itself |
| 90 | Write `mean(data)`, `variance(data)`, `std_dev(data)` from scratch. Apply to `[2,4,4,4,5,5,7,9]`. | Dispersion | **Every metric dashboard has variance.** Std-dev of latency is your error budget's noise floor |
| 91 | Write `median(data)` and `mode(data)`. Run all three on the same dataset and print where they diverge. | Central tendency | **p50 vs p99 vs mean.** Always report percentiles for latency; the mean hides tail latency |
| 92 | Write `quartiles(data)` → Q1, Q3, IQR, and `find_outliers(data)` using the 1.5×IQR rule. | Quartiles | Box plots in dashboards, outlier detection in metrics, data-quality validation |
| 93 | Write `empirical_rule(data)` — report % within 1, 2, 3σ and flag outliers on a normal-ish dataset. | Empirical rule | **3-sigma alerting** and anomaly thresholds in monitoring |
| 94 | Write a program that computes correlation of `x` vs `x²` (≈1.0) and then demonstrates in comments why causation doesn't follow. | Correlation ≠ causation | Debugging: two things move together in production. The third factor is usually a deploy |
| 95 | Write `simple_random_sample(pop, n)` and `stratified_sample(pop, strata, n)`. Compare the means of 100 samples each. | Sampling | Log sampling, trace sampling, per-tenant fairness in canary rollouts |
| 96 | Write `clt_simulation(n_trials)` — roll 2 dice 10,000 times, plot the distribution of sample means. | CLT | Why aggregating more instances makes latency stable; capacity forecasting confidence |
| 97 | Write `combos_with_repetition(n, r)` for picking 5 fruits from 3 kinds. | Combinations w/ repetition | Multi-select UIs, tag combinations, unordered feature bundles |
| 98 | Write `simulate_coin_game(rounds)` for the $1-for-HH / $3-for-TT game. Run 10,000 rounds and report total profit. | Simulation | Monte Carlo: you cannot derive it, so you sample it. Load tests, chaos testing, risk analysis |

---

### Level 5 - Calculus intuition (Problems 99–113)

You are **not** a mathematician. You are learning to reason about *rates of change and accumulated change*, because that is what performance analysis is.

| # | Problem | Skill |
|---|---|---|
| 99 | Write `limit_of_square(x_target)` that evaluates `x²` at `x_target ± 0.01, ± 0.0001, ± 1e-8` and prints the convergence table. | Limit intuition | Convergence: why `n/large_n → 0`, why a cache hit asymptotically wins, what "eventually consistent" means |
| 100 | Write four functions exhibiting a removable discontinuity, a jump, a vertical asymptote, and diverging to infinity — plus `classify_discontinuity(f, point)`. | Discontinuity types | **Circuit breakers and rate limiters are discontinuities.** Buckets reset → a step function. This is why token buckets are lumpy |
| 101 | Write `derivative_by_definition(f, x)` implementing `(f(x+h) - f(x)) / h`. Use it on `x²` with shrinking `h` and watch it converge to `2x`. | Derivative definition | The basis of numerical differentiation — auto-diff in ML, `scipy.gradient`, sensitivity analysis |
| 102 | Write `power_rule`, `sum_rule`, `constant_multiple_rule`. Verify the power rule numerically against #101. | Rules | Differentiating a cost function to find where it's cheapest |
| 103 | Write `d_sin`, `d_cos`, `d_exp`, `d_log`. Verify `d_sin` numerically against your #113 derivative. | Standard derivatives | Signal processing, oscillating systems, exponential curve-fitting, damped-oscillation tuning |
| 104 | Write `chain_rule_demo()` for `(3x²+1)⁵`, differentiating inner then outer. | Chain rule | **Backpropagation is the chain rule.** Every neural network trained end-to-end uses this |
| 105 | Write `critical_points(f, a, b)` that finds zeros of `f'` and classifies each as max or min by sampling either side. | Extrema | Finding the optimal operating point: best batch size, cheapest threshold, peak throughput |
| 106 | Write `max_volume_box(surface_area)` — open-top box from 1000 cm² of material, found by **searching** l×w×h rather than by calculus. Then confirm with calculus. | **Optimization classic** | Container sizing, shard count, batch size — you can search instead of deriving. Know both |
| 107 | Write `s(t) = t³ - 4t²`, `v(t)`, `a(t)`. Find where it turns around and when it changes direction. | Motion | Queue depth over time, backlog drain rate, "when does the spike clear?" |
| 108 | Write `implicit_derivative(F, x, y)` using your numerical derivative, applied to `x² + y² = 25` and `x² + y³ = 8`. | Implicit diff | Solving coupled equations when you can't isolate one variable — Newton's method, `scipy.optimize.root` |
| 109 | Write `riemann_left(f, a, b, n)` and approximate the area under `y = x²` from 0 to 3. | Integration idea | **Area under a curve = accumulated total.** CPU-seconds consumed, bytes transferred, cumulative requests |
| 110 | Run #109 for n = 10, 100, 1000, 100000 and watch it converge to exactly 9. Plot the error. | FTC | `prometheus` `rate()` and `increase()` are literally numerical integrals over time |
| 111 | Write antiderivatives for `2x³`, `sin(x)`, `eˣ`. Then a substitution-based integral of `(2x)·2x`. | Integration | Deriving cumulative totals from rate functions |
| 112 | Write a generic `riemann(f, a, b, n)` that works for any function, with left/right/midpoint modes. | Numeric integration | Numerically integrating any metric without a closed-form formula — no calculus needed |
| 113 | Write `numerical_derivative(f, x, h)` and compare it against every analytic derivative you wrote in #102–#104. | Numerical gradient | Auto-differentiation, gradient checking in ML frameworks, numerical optimization |

---

### Level 6 - Discrete math, graphs & logic (Problems 114–130)

The math of "things you can count." This is where systems thinking comes from.

| # | Problem | Skill |
|---|---|---|
| 114 | Write `truth_table(expr)` — a generator that evaluates a boolean expression over all 2ⁿ inputs and prints the table. Run it on `not (A and (B or C))`. | Boolean logic | Every `if` statement. Precedence bugs between `and`/`or` and SQL `WHERE` clauses |
| 115 | Write `negate(expr)` for "A and not B", generate its truth table, and assert it matches De Morgan's `(not A) or B`. | De Morgan | Simplifying and flattening filter expressions; optimizing boolean query predicates |
| 116 | Write `implication_variants(P, Q)` printing the truth values of P→Q, its converse, inverse, and contrapositive, and flagging which pairs are equivalent. | Implication | **Type systems and validation**: if it's a valid `int`, it must be usable as one. The contrapositive is how you write error messages |
| 117 | Write `equivalent(e1, e2)` that compares two expressions by exhaustive truth table. Prove `(A or B) and (A or C)` ≡ `A or (B and C)`. | Boolean algebra | Two different-looking conditions that behave identically — refactoring without changing behaviour |
| 118 | Write a program printing `0 & True` vs `0 and True`, and `[] & [1]` vs `[] and [1]`. Explain each surprise in comments. | Bitwise vs logical | **The single most common Python bug**: `&`/`|` on non-booleans. Filter lists without TypeErrors |
| 119 | Write `set_ops(a, b)` → union, intersection, difference, symmetric difference. Apply to A={1,2,3,4}, B={3,4,5}. | Set theory | **SQL `UNION` vs `INTERSECT`.** Set-based authorization, tag filtering, dedup, permission models |
| 120 | Draw a labelled 3-set Venn with `matplotlib`, shading each of the 7 regions, and compute a union from the picture. | Venn diagrams | Overlapping user segments; finding "customers in A and B but not C" for a campaign |
| 121 | Write `inclusion_exclusion(total, a, b, both)` for the students problem. Return how many take neither. | Inclusion-exclusion | Counting with overlap: "unique users who did X or Y", multi-condition analytics |
| 122 | Write `pigeonhole(items, boxes)` that brute-forces the smallest number of items guaranteeing a collision in `boxes` rooms. Test 13/4, then find the minimum for 5 rooms. | **Pigeonhole** | **Hash collisions are guaranteed, not unlikely.** Bounded caches, limited ports, finite ID spaces |
| 123 | Build a graph with 5 vertices and 7 edges, write `degree_table(adj)`, and assert the handshaking lemma holds. | Graph basics | Microservice dependency graphs; finding the most-called service; detecting circular dependencies |
| 124 | Encode the 7 bridges of Königsberg as an adjacency matrix, then brute-force search for an Euler path. Prove none exists. | Euler paths | Route planning with no repeats, network packet walks, "can I ship all logs with one pipeline?" |
| 125 | Write `has_hamiltonian_path(graph)` via backtracking. Test it on a 6-node graph with a known answer. | Hamiltonian | Traveling-salesman-shaped problems: optimal delivery routes, optimal test sequences, NP-hard discovery |
| 126 | Write `bfs(graph, start)` and `dfs(graph, start)`. Run both on a 7-node graph and print the traversal order. | Traversal | **Web crawling.** BFS for shallow discovery, DFS for deep scraping. Also dependency resolution |
| 127 | Write `topological_sort(graph)` for a course-prerequisite graph. Count how many valid orderings exist — is it unique? | Topological sort | **Build systems (make, Docker layer order), DAG workflows (Airflow), plugin load order, schema migrations** |
| 128 | Build a binary tree from `[8,3,10,1,6,14,4,7,13]` and print in-order, pre-order, and post-order. | Trees | **B-trees are database indexes.** Also: ASTs, file systems, heaps, decision trees in ML |
| 129 | Write `recurrence_steps(n, kind)` for `T(n)=2T(n/2)+n` and `T(n)=2T(n/2)`, plot both on a log scale, and label which is `O(n log n)`. | Recurrences | Predicting runtime as n grows. Decide algorithm by recurrence, not by vibes |
| 130 | Build an array indexed by `hash(x) % 16` with 1000 colliding keys and measure the slowdown. Then implement a fix and benchmark it. | Modular arithmetic & hashing | **Dict internals.** Open addressing, load factor, why poorly-distributed keys destroy performance |

---

### Level 7 - Advanced & engineering-relevant (Problems 131–150)

The "why the machine is fast / secure / big" layer.

| # | Problem | Skill |
|---|---|---|
| 131 | Write `dot(a, b)` from scratch. Compute (1,2,3)·(4,5,6) and project `b` onto `a` — then explain what the projection means geometrically. | Vector ops | **This is vector search.** Dot product / cosine similarity is how every embedding search, RAG retriever, and recommendation engine scores relevance |
| 132 | Write `cross(a, b)` for 3-vectors. Compute (1,0,0)×(0,1,0) and use the right-hand rule to explain the result. | Cross product | Finding surface normals for lighting/rendering, torque in physics engines, triangle winding order in meshes |
| 133 | Write `norm(v, order)` for L1 and L2. Show why L2 is what gradient descent cares about by plotting both. | Norms | **L2 = the MSE loss function.** L1 for robust outliers. Norms are "how big is this error?" |
| 134 | Write `matmul(A, B)` with triple nested loops. Multiply a 2×3 by a 3×2 and verify against `numpy.matmul`. | Matrices | **Every neural network forward pass is matmul.** Also image transforms, state-space systems |
| 135 | Write `apply_matrix(M, v)`. Use it to rotate (1,0) by 90° and confirm the length is preserved. | Linear transforms | Coordinate-system conversion, camera/view/projection matrices, game rendering pipelines |
| 136 | Write `determinant_2x2(M)`. For `[[2,1],[1,3]]`, apply it to two shapes and show what the result *means*. | Determinant | Detecting singular matrices — a zero determinant means the transform collapses space (broken config or degenerate matrix) |
| 137 | Write `gauss_eliminate(A, b)` with partial pivoting. Solve a 3×3 system and verify by substituting back. | Gaussian elimination | Solving simultaneous constraints numerically; least-squares fitting; circuit and structural analysis |
| 138 | Write `eigenvalues_2x2(M)` from the characteristic polynomial. Compute for `[[2,0],[0,3]]`, then apply it to a 100×100 page-rank-style matrix. | Eigen intuition | **PageRank is an eigenvector problem.** Also PCA, stability analysis, SVD compression, spectral clustering |
| 139 | Write `benchmark_loop_vs_numpy(n)` timing a 10M-element loop against a NumPy vectorized op. Print the speedup ratio. | Vectorization | **Understanding *why* NumPy is fast.** The same lesson explains why SQL beats a Python loop over the same rows |
| 140 | Write `why_float_error()` that prints the binary representation of `0.1`, `0.2`, and their sum. | Float precision | **Every money bug in every codebase.** Why you use `Decimal`, integer cents, or a payments library |
| 141 | Write a program timing arithmetic on 64-bit ints vs 4096-bit ints to show what Python's bignums actually cost. | Bignums | Why `int` is unlimited but not free; performance of crypto and big-number arithmetic in Python |
| 142 | Write `bit_and`, `bit_or`, `bit_xor`, `bit_not` for a single byte using only shifts and masks. Verify against the `&`, `\|`, `^` operators. | Bitwise ops | Subnet masks, file permissions, flag enums, protocol headers, parsing binary formats |
| 143 | Write `count_set_bits(n)`, `clear_lowest_bit(n)`, `is_power_of_two(n)`. Then implement each in one clever line and compare. | Bit hacks | Hamming distance, bitmasking sparse sets, checking power-of-two capacities (bucket sizing, sharding masks) |
| 144 | Write `bad_hash()` (e.g. returning the last digit), insert 1000 keys, and print the collision count. Then implement a better one. | Hashing & collisions | Dict/HashMap internals, cache key design, **hash-flooding DoS attacks**, why hash salts exist |
| 145 | Write `count_comparisons(sort_fn, data)` — instrumented bubble sort vs merge sort at n = 10, 16, 32. Plot comparisons vs n on a log scale. | Complexity | Why an `O(n²)` sort dies at 100k rows. The basis of every index and query-plan decision |
| 146 | Write `bytes_to_human(n)` printing both the SI (1000) and IEC (1024) readings. Explain why both exist in a docstring. | Units & memory | Docker image sizes, disk quotas, bandwidth (Mbps vs MB/s), log-volume capacity planning |
| 147 | Write `ncr_mod_p(n, r, p)` computing C(52,5) and then C(52,5) mod 1e9+7. Time it for large inputs. | Combinatorics in code | Dynamic programming on combinatorics (counting paths), competitive-programming modulo, crypto key math |
| 148 | Write `nim(a, b)` finding the winning move for (3,4). Implement a brute-force solver and let it confirm your strategy. | Game theory | Minimax in game AI; adversarial strategy; also "optimal play" in bidding/pricing and load-balancing strategy games |
| 149 | Write `bits_needed(n)` and `entropy(probs)` in bits. Compare a fair coin to a biased one. | Information theory | **Data compression, entropy coding, hashing randomness, log-level design, cryptographic randomness quality** |
| 150 | Write `mod_pow(base, exp, mod)` printing every squaring step. Use it on `pow(7, 13, 11)`. Then write RSA's core idea in the docstring. | Modular exponentiation | **The engine behind RSA, SSH keys, TLS handshakes, and blockchain.** Big-number crypto at the core of security |

---

### Phase 1 Exit Gate

- [ ] **T1–T30 warm-up complete** - every one committed and running
- [ ] **150/150 written as programs**, each with a docstring, printed intermediate values, and at least one assertion
- [ ] Zero use of a library that solves the task for you (no `sympy`, no `math.gcd`, no `numpy.linalg.eigvals`)
- [ ] Problems 140, 143, 145, 150 redone cold from scratch after 2 weeks
- [ ] Problems 3, 21, 28, 61, 81, 101, 122, 130, 134 re-implemented as a small reusable library with a test suite
- [ ] `NOTES.md` contains a **"Where I've seen this"** entry for all 180 tasks — each naming a concrete real prior (a library, a bug, a feature), not a vague one
- [ ] For the 20 problems you found most abstract (dot product, cross product, eigenvalues…), you can name a **specific system you have used** that depends on them
- [ ] You can explain, without notes, *why* each of the 8 levels exists in software
- [ ] Every problem's code runs from a clean checkout with no leftover global state

**Deliverable:** a `phase1/` repo with 180 files:

```
phase1/
  warmup/t001_hello_world.py ... t030_unit_converter.py
  level0/problem_001.py ... problem_020.py
  level1/ ... level7/
  library/          # the 9 reusable implementations
  tests/
  NOTES.md          # per level: what broke, what surprised you, what you'd do differently
```

**Suggested pace:** T1–T30 in 1 week. Then 2 problems per day on Levels 0–1, slowing to 1 per day by Level 4, and 1 per 2 days for Levels 5–7. Total ≈ 8 weeks.

---

## Phase 2 - Python & OOP

> Python first, OOP second - but they are taught together because that's the only way OOP makes sense.

### Part A - Python the language (2–3 weeks)

Do not skip this. OOP without fundamentals is memorizing syntax.

| Topic | Must be able to do |
|---|---|
| Values & types | int, float, str, bool, None, type conversion, `is` vs `==` |
| Control flow | if/elif/else, while, for, break, continue, nested loops |
| Data structures | `list`, `tuple`, `dict`, `set` - mutability, slicing, comprehension |
| Functions | args, kwargs, defaults, *args, **kwargs, return, scope (LEGB), lambdas |
| Comprehensions | list/dict/set comprehension, nested, conditional |
| Errors | `try/except/else/finally`, raising, custom exceptions |
| Files | `open`, context manager `with`, read/write/append, CSV, JSON |
| Modules | import, `__name__`, packages, `pip`, requirements, venv usage |
| OOP basics | class, `self`, `__init__`, instance vs class attributes, methods |
| Iteration | `__iter__`, `__next__`, generators (`yield`), `itertools` |
| Typing | type hints, `Optional`, `Union`, generics, `dataclasses`, `TypedDict`, `Protocol` |
| stdlib you'll actually use | `pathlib`, `datetime`, `random`, `collections`, `itertools`, `functools`, `re`, `json`, `subprocess`, `os`, `sys` |
| Testing | `pytest`, fixtures, parametrize, coverage, test doubles |

**Checkpoint projects:**
1. CLI calculator (REPL: `add 2 3`, `div 10 0` → friendly error)
2. Log file analyzer (parse, count errors per hour, output a report)
3. CSV → clean JSON transformer (real messy data from a public dataset)

### Part B - OOP concept ladder (4–6 weeks)

Build each concept *in isolation* before it enters a project. Each rung has three parts:

- **Toy** — the ~20-line program that isolates the concept. No project. No cruft.
- **Trap** — the classic mistake that means you memorized the syntax but don't own it. Break it on purpose, then fix it.
- **Where you'll see it** — name one concrete system that uses it. If you can't, you don't know it yet.

#### 1. Classes & objects
- **Toy:** `Point(x, y)` with `translate(dx, dy)` (returns a *new* point) and `distance_to(other)`.
- **Trap:** forgetting `self`, and shadowing an attribute (`x = 5` inside a method instead of `self.x`).
- **Where you'll see it:** every ORM model, every `open()` returns a file object, every Flask route is a function but its context is a class.

#### 2. Class vs instance state
- **Toy:** `Counter` that tracks its own value (instance) and a `total_instances` count (class). Then deliberately write `def buggy(items=[])` and watch two calls share one list.
- **Trap:** the mutable default argument. Also: mutating shared class state unexpectedly.
- **Where you'll see it:** sequence IDs, connection-pool size limits, singleton-ish config objects, `dict`'s internal counters.

#### 3. Encapsulation
- **Toy:** `BankAccount` where `balance` can only change via `deposit()` / `withdraw()`; read access via `@property`; one deliberate bad setter that raises `ValueError` on negative.
- **Trap:** `self.balance = ...` scattered across methods; "convenient" public fields you regret in week 3.
- **Where you'll see it:** API clients that hide tokens, config objects, `decimal`-based money fields.

#### 4. Inheritance & `super()`
- **Toy:** `Vehicle → Car → ElectricCar`, print `type(self).__mro__`, then build a diamond with two "mixins" and read the order `super()` resolves.
- **Trap:** `super()` without arguments in multiple inheritance; a 5-deep hierarchy that forces a 5-file edit for one feature.
- **Where you'll see it:** `Exception` hierarchy, `xml.etree` Element classes, framework base classes you extend (FastAPI routes, Django models).

#### 5. Polymorphism
- **Toy:** `make_sound()` on `Duck`, `RobotDuck`, `SilentDuck`; call it on a mixed list without `isinstance`.
- **Trap:** `isinstance` checks where duck typing should be — the `if isinstance(x, A)` / `elif isinstance(x, B)` spiral.
- **Where you'll see it:** dispatch to handlers, serializers that work on any model, `sorted()` working on mixed-but-comparable types.

#### 6. Abstraction
- **Toy:** `Shape` as `abc.ABC` with `@abstractmethod area()` + `perimeter()`; concrete `Circle`, `Square`; then the same thing as a `typing.Protocol` and compare.
- **Trap:** abstract base classes that aren't actually abstract (one concrete method that everyone copies-pastes).
- **Where you'll see it:** repository pattern, transport abstractions (HTTP client vs test double), driver interfaces.

#### 7. Class methods & static methods
- **Toy:** `Fraction.from_decimal(0.5)` and `Point.from_polar(r, theta)` as `@classmethod` factories; a `@staticmethod` validator for a task status string.
- **Trap:** `@classmethod` reaching into instance state (impossible) or `@staticmethod` doing nothing but pretending.
- **Where you'll see it:** `dict.fromkeys`, `datetime.fromisoformat`, `Path.from_parts` — all factories you already use.

#### 8. Dunder methods
- **Toy:** a `Vector` with `__add__`, `__mul__` (scalar), `__repr__`, `__eq__`, `__hash__`, `__len__`, `__iter__`, `__getitem__`, `__bool__`; plus a `Timer` context manager (`__enter__`/`__exit__`) and a callable `RateLimiter` (`__call__`).
- **Trap:** defining `__eq__` without `__hash__` and breaking dicts; `__repr__` that raises on missing optional attrs.
- **Where you'll see it:** every `list`/`dict`/`pathlib.Path` you use daily is just a bag of dunders.

#### 9. Composition over inheritance
- **Toy:** refactor a `MobileDevice` hierarchy (`Phone`, `Tablet`, `SmartWatch` each with screen/battery/OS subclasses) into `Device` *has* `Screen`, `Battery`, `OSSystem`. Same behaviour, smaller diff surface.
- **Trap:** "inheritance for code reuse" — copying a base class you only need 2 methods from.
- **Where you'll see it:** ORM relationships (has-a), decorator composition, middleware stacks.

#### 10. Mixins
- **Toy:** `SerializableMixin` (`to_dict` / `from_dict`) and `TimestampedMixin` (`created_at` / `updated_at`); class `Event(SerializableMixin, TimestampedMixin)`; break the `super().__init__` chain on purpose.
- **Trap:** mixins that require base-class methods nobody checked; `super()` chain broken in a diamond.
- **Where you'll see it:** `TimestampedModel` in Django, capability mixins in game engines, FastAPI dependency stacking.

#### 11. Dataclasses, Enums, NamedTuple
- **Toy:** `Task` dataclass with `__post_init__` validation (priority must be a known string); `Status` Enum with a `color` computed property; frozen `Point` NamedTuple.
- **Trap:** dataclass with mutable default (`tasks: list = []`); Enum members used as dict keys then compared with `==` on strings.
- **Where you'll see it:** config models, protocol constants, API schemas (Pydantic is dataclass-adjacent for a reason).

#### 12. SOLID — one refactor each
- **Toy:** start with a 200-line `OrderProcessor` god class; do five surgical refactors:
  - **SRP:** split validation, pricing, persistence into three classes.
  - **OCP:** discount rules become pluggable strategies (add "student 10%" without touching the processor).
  - **LSP:** `DatabaseConnection` and `InMemoryConnection` must both satisfy the same contract — find the method that breaks it.
  - **ISP:** split a fat `Worker` interface into `Codable`, `Serializable`, `Comparable`.
  - **DIP:** inject a `Clock` instead of calling `datetime.now()` in 14 places.
- **Trap:** "refactoring" that renames things without changing dependencies.
- **Where you'll see it:** any framework worth using. This is the skill interviewers probe in "tell me about a design you changed".

#### 13. Error hierarchy
- **Toy:** `AppError` → `ValidationError` / `NotFoundError` / `ConflictError`; catch `NotFoundError` specifically and let `AppError` bubble; chain with `raise ... from e`.
- **Trap:** bare `except:`; raising `ValueError` for "user not found" because it's the closest builtin.
- **Where you'll see it:** `httpx.HTTPError` tree, `sqlalchemy.exc` tree, `urllib.error` — every serious library has one.

#### 14. Dependency injection
- **Toy:** `SearchEngine(client: HttpClient)`; constructor injection; test with a `FakeHttpClient` that records calls. Then method injection for one dep and write down the tradeoff.
- **Trap:** `open()` / `requests.get()` hardcoded inside business logic → untestable, no swap, no config.
- **Where you'll see it:** FastAPI's `Depends()`, Spring, DI in every major framework. This is *the* testability unlock.

#### 15. Design patterns in Python
- **Toy per pattern, ~30 lines each:**
  - **Strategy** — sort strategies (`sort_by_date`, `sort_by_priority`); select at runtime.
  - **Factory** — build a `PaymentGateway` from a config string (`stripe` / `mock`).
  - **Observer** — event bus: `publish("user.created", payload)` → N subscribers fire; one subscriber crashing must not stop others.
  - **Decorator** — Pythonic function decorator: `@retry(times=3, backoff=2)` and `@log_call`.
  - **Singleton** — implement it, then write a comment on why you'll avoid it in real code (global state, test hell).
  - **Iterator** — a lazy Fibonacci/URL-walk iterator with `__iter__` / `__next__`.
  - **State** — vending-machine FSM: INSERT_COIN → SELECT → DISPENSE → REFUND; `fire(event)` in a state where it's illegal raises with the current state in the message.
  - **Template Method** — `Report` base with fixed skeleton, `render_header` / `render_body` / `render_footer` left to subclasses.
  - **Command** — undo/redo stack for a text editor (STORE, UNDO, REDO).
- **Trap:** pattern theater — naming a class "Factory" that just calls `__init__`.
- **Where you'll see it:** FastAPI background tasks (Command-ish), SQLAlchemy events (Observer), `functools.lru_cache` (memoization), `asyncio` callbacks (decorators of a sort).

**For every concept:** the toy program + a `NOTES.md` entry answering "where have I seen this?" + the deliberate trap, broken and fixed. Commit per rung.

### Part C - The project ladder

**Rules that apply to every project, every tier:**
1. **It must pass its own numbered requirements (R-lists) below.** A requirement you can't meet gets written in the README as a known gap — silent skipping is a fail.
2. **Custom exceptions, not strings.** No `raise "error"`; no stringly-typed return codes. Every project defines its own exception tree (listed under its requirements): one base error the app/CLI catches, concrete errors the logic raises. Catching bare `Exception` at the top level is a fail.
3. **A `pytest` suite that runs in under 30 seconds.** No network, no sleeps > 50ms, no "flaky" tests.
4. **A README with:** what it does, architecture diagram (boxes + arrows, ASCII fine), key design decisions (inheritance vs composition, where each pattern lives, and where each exception type gets caught), how to run it.
5. **Type hints on every public function.**

#### Tier 1 - Playful (1 project per week)

**1. Animal kingdom simulator** — a console app simulating a farm of animals.

Functional requirements:
- R1: `Animal` base class: `name`, `species`, `hungry: bool`; `make_sound()` and `move()` defined.
- R2: At least 4 concrete species (`Dog`, `Cat`, `Bird`, `Fish`) each overriding sound + movement (`Bird.move` → "flies", `Fish.move` → "swims").
- R3: `Farm` holds animals: `add`, `remove`, `feed_all()` (feeding a hungry animal un-hungers it; feeding a fed animal is a no-op that logs).
- R4: `Farm` is iterable and countable: `for a in farm`, `len(farm)`.
- R5: Hungry animals produce a different (longer) sound than fed ones.
- R6: Polymorphic `Farm.loudest_sound()` returns the longest sound using only the base-class interface (no `isinstance`).
- R7: `stats()` returns per-species counts.
- R8: `save(path)` / `Farm.load(path)` — JSON round-trip preserves state, including hunger.
- R9: Adding a new species (`Robot`?) requires zero changes to `Farm` — OCP, and a test proves it.
- R10: ≥10 tests, including the OCP test and a serialization round-trip.

Exceptions (raise these — all subclass the first one):
- `FarmError` — base for everything the farm raises
- `AnimalNotFoundError` — removing / feeding / inspecting a name that isn't in the farm
- `DuplicateNameError` — adding an animal whose name already exists
- `InvalidSpeciesError` — species string that isn't a known species
- `CorruptFarmFileError` — load() hits malformed JSON (message names the file)

**2. Shape zoo + area calculator** — a library plus a CLI that computes and compares geometry.

Functional requirements:

- R1: `Shape` ABC with abstract `area()` and `perimeter()`.
- R2: `Circle`, `Rectangle`, `Triangle` (Heron's formula — must reject degenerate triangles), `Trapezoid`.
- R3: Shapes are comparable: `__eq__` (equal area within 1e-9), `__lt__` (smaller area), `sorted([sh...])` works.
- R4: `shape * 2` returns a scaled copy (`__mul__`), original unchanged.
- R5: `__repr__` round-trips: `eval(repr(shape))` recreates it — test it.
- R6: CLI: `shapes.py area circle 5`; `shapes.py compare circle 5 rectangle 3 4` prints which is larger and by how much.
- R7: Invalid dimensions (negative radius, zero-length side) raise `ValueError` with a helpful message; CLI prints it and exits 1.
- R8: `report(shapes)` prints a table: name, area, perimeter, plus total area.
- R9: Known-value tests: `Circle(1).area() == math.pi`, triangle with sides 3-4-5 has area 6.

Exceptions (raise these — all subclass the first one):
- `ShapeError` — base
- `InvalidDimensionError` — negative radius, zero or negative side
- `DegenerateTriangleError` — triangle inequality violated (sum of two sides <= third)
- `ScaleError` — scale factor not > 0

**3. Playlist manager** — a music library with persistence.

Functional requirements:

- R1: `Track` dataclass: `title`, `artist`, `duration_sec`; `__str__` formats as `"Artist - Title (3:45)"`.
- R2: `Playlist`: add (duplicate exact match rejected with `DuplicateTrackError`), remove by index or title, `__len__`, `__iter__`, `__getitem__` (negative indexing works).
- R3: `total_duration()` returns seconds; `__format__` renders h/m/s.
- R4: `search(query)` — case-insensitive substring on title OR artist, returns matches in order.
- R5: `shuffle(seed)` — deterministic given a seed; reshuffle without seed is random.
- R6: `save(path)` / `load(path)` JSON round-trip.
- R7: `merge(other)` — no duplicates, order preserved, returns the new total length.
- R8: Context manager: `with Playlist() as pl:` auto-saves on exit even if an exception is raised inside.
- R9: ≥12 tests including shuffle-determinism and merge-dedup.

Exceptions (raise these — all subclass the first one):
- `PlaylistError` — base
- `DuplicateTrackError` — add() of an exact duplicate (message includes the existing track's index)
- `TrackNotFoundError` — remove() by out-of-range index or unmatched title
- `CorruptPlaylistFileError` — load() of a malformed or invalid-structure JSON file

**4. Blackjack** — user vs dealer, chips, full rules.

Functional requirements:

- R1: `Card` (rank, suit); `Deck` with `__iter__`, `shuffle()`, `deal()`; a fresh deck has exactly 52 unique cards (asserted in a test).
- R2: `Hand`: `value()` resolves aces as 11 or 1 optimally; `is_bust`, `is_blackjack`, `__len__`.
- R3: `Dealer` always stands on 17, hits below.
- R4: Game loop: `hit` / `stand` / `double`; chips start at 100; betting below balance raises `InsufficientChipsError`.
- R5: Outcomes are an Enum: `WIN`, `LOSE`, `PUSH`, `BLACKJACK`; payout table: 1:1, 3:2 for blackjack.
- R6: `stats()` after a session: hands played, win rate, total chips, longest streak.
- R7: Replay: the game records every action; `replay( actions , seed )` reproduces the exact same hand — test it.
- R8: Edge-case tests: 5-card ace hand (A-A-A-A-A = 21), double when broke, insurance not implemented (document as known gap).

Exceptions (raise these — all subclass the first one):
- `BlackjackError` — base
- `InsufficientChipsError` — bet greater than the current balance
- `InvalidBetError` — bet that is zero, negative, or not an integer
- `DeckEmptyError` — dealing from an exhausted deck (document your reshuffle policy)
- `GameAlreadyOverError` — hit / stand / double after the hand has ended

**5. Tic-Tac-Toe engine** — pure game logic, no UI.

Functional requirements:

- R1: `Board` supports `"A1"`–`"C3"` coordinate indexing via `__getitem__` / `__setitem__`; invalid coordinates raise `InvalidMoveError`.
- R2: `Game` with a `Phase` enum: `PLAYING`, `X_WON`, `O_WON`, `DRAW`.
- R3: `game.move("B2")` validates: square occupied, game already over, out of range — each raises a distinct error type.
- R4: `winner()` detects all 8 winning lines (3 rows, 3 cols, 2 diagonals).
- R5: `minimax()` — a perfect AI that never loses; a "difficulty" parameter injects random mistakes.
- R6: `undo()` — one move at a time, to the start of the game; `undo` after the start raises.
- R7: `__str__` renders the board in ASCII with coordinates.
- R8: Test: 100 random games vs minimax — player never wins; full legal/illegal move table tested.

Exceptions (raise these — all subclass the first one):
- `GameError` — base
- `InvalidCoordinateError` — move outside A1..C3
- `SquareOccupiedError` — move onto a filled square
- `GameAlreadyOverError` — move after a win or draw (matches R3: distinct error types)
- `NothingToUndoError` — undo() with no moves made yet

**6. Dice game simulator** — a probability game with a stats report.

Functional requirements:

- R1: `Die(sides)` with a fairness check: 6000 rolls, per-face count within ±15% of expected (a "is it loaded?" test you run yourself).
- R2: `Player` hand of up to 5 dice: `roll()`, `keep(dice)`, `reroll()` — max 3 rolls, extra attempts raise.
- R3: Score combinations: pair, three-of-a-kind, full house, straight, 21 — a pure `score_hand(dice)` function.
- R4: `Game` plays rounds between 2 players, declares a winner, handles ties.
- R5: `Simulator` runs N full games between two strategies — `GreedyStrategy` (keep any 3+) and `ExpectedValueStrategy` (keep only EV-positive rolls) — and prints a head-to-head win-rate table.
- R6: Seeded RNG throughout; `--seed` CLI flag makes any run reproducible.
- R7: Tests: `score_hand` lookup table (≥10 cases), fairness test, strategy sanity (EV strategy wins ≥50% of 10k games).

Exceptions (raise these — all subclass the first one):
- `DiceError` — base
- `InvalidDieSidesError` — Die(sides) with sides < 2
- `HandTooLargeError` — adding a 6th die
- `RollLimitExceededError` — attempting a 4th roll
- `InvalidKeptDiceError` — keep() referencing a die that isn't in the hand

**7. Bank account simulator** — a mini bank with hard invariants.

Functional requirements:

- R1: `Account` base: `owner`, `opened_at`; balance **can never be negative** — this invariant is asserted in tests after every possible operation.
- R2: `SavingsAccount` (monthly interest, no overdraft) and `CheckingAccount` (overdraft limit −500, fee of 5 per overdraft day).
- R3: Every mutation returns an immutable `Transaction` ledger entry; `statement(since, until)` returns a sorted ledger slice.
- R4: `transfer(from_acct, to_acct, amount)` is atomic: if validation fails midway, neither balance moves — test with a transfer that must fail.
- R5: Custom exception tree: `InsufficientFundsError`, `AccountFrozenError`, `ClosedAccountError`, all subclassing `BankError`.
- R6: `Bank.process_month()` applies interest to every savings account; prints a summary line per account.
- R7: `__repr__` masks account numbers: `CheckingAccount(owner='Ada', number='****42')` — no full number ever printed or logged.
- R8: ≥15 tests: the invariant test, atomic-transfer test, frozen-account test, interest math test.

Exceptions (raise these — all subclass the first one):
- `BankError` — base (matches R5)
- `InsufficientFundsError` — withdraw / transfer exceeds available balance (message states the shortfall, not the full balance)
- `AccountFrozenError` — any operation on a frozen account
- `ClosedAccountError` — any operation on a closed account
- `InvalidTransferError` — amount <= 0, or source and destination are the same account

**8. Inventory / warehouse system** — multi-warehouse stock with alerts.

Functional requirements:

- R1: `Item` (sku, name, unit_cost); SKU validated by regex `^[A-Z]{3}-\d{3}$` with `InvalidSkuError`.
- R2: `Warehouse`: `receive(sku, qty)`, `dispatch(sku, qty)` raises `OutOfStockError` with current level in the message; negative qty always raises.
- R3: `transfer_to(other, sku, qty)` is atomic across two warehouses (one gains exactly what the other loses).
- R4: `Inventory` holds N warehouses: `total_stock(sku)`, `locate(sku)` → which warehouses have it, `valuation()` → total asset value.
- R5: Low-stock alerts: `register_alert(observer, threshold)` — Observer pattern practice; `dispatch` crossing the threshold fires exactly one alert.
- R6: `turnover(sku)` = dispatched / received for a period; `slow_movers()` returns items below a turnover ratio.
- R7: JSON persistence: `save()` / `load()`; round-trip test; loading a corrupt file raises `CorruptInventoryError`, never a traceback.
- R8: `__len__` = total unit count across warehouses; `__contains__("sku")` = has any stock.
- R9: A "interleaving" test: a scripted sequence of receive/dispatch/transfer that can't drive any stock negative.

Exceptions (raise these — all subclass the first one):
- `InventoryError` — base
- `InvalidSkuError` — SKU failing the `^[A-Z]{3}-\d{3}$` regex
- `UnknownItemError` — operating on a SKU that has never been received
- `OutOfStockError` — dispatch exceeding the available level (message includes the current level, matches R2)
- `InvalidQuantityError` — quantity <= 0 on receive / dispatch / transfer
- `CorruptInventoryError` — load() of a malformed file (matches R7: never a raw traceback)

**9. Snake (text-grid version)** — classic snake, terminal-rendered, with a headless mode.

Functional requirements:

- R1: `Board(width, height)` with `__contains__`; `wrap: bool` option (wall vs wrap-around).
- R2: `Snake` as a `deque` of points: `grow()`, `head`, `will_collide(point)`.
- R3: `Food` spawns on a random free cell (seeded RNG); never on the snake; regrows after eating.
- R4: `Game` loop: direction input, tick, score; game over on self-collision or wall (unless wrap).
- R5: Direction is a **queue**: two turns in one tick are applied in order, and a 180° reversal is rejected (`InvalidDirectionError`).
- R6: High score persisted to a file; `--replay` replays a saved input script deterministically.
- R7: `__str__` renders the board with the snake in `O`, food in `*`, wall in `#`.
- R8: Headless: `Game.run(input_script)` — no keyboard, no sleep; ≥5 scripted test scenarios: eat & grow, self-collision, wall-collision, wrap mode, new high score.

Exceptions (raise these — all subclass the first one):
- `GameError` — base
- `InvalidDirectionError` — 180° reversal queued as the next move (matches R5)
- `InvalidReplayScriptError` — malformed input script (unknown token, out-of-range move)
- `CorruptScoreFileError` — unreadable high-score file (decide + document: raise and let CLI reset it to 0)

**10. Contact book with persistence** — a phone-book CLI.

Functional requirements:

- R1: `Contact`: name, phones (multiple), email, tags (set), notes; phones normalized to E.164 (`"07-911-123456"` → `"+9717911123456"` — document your assumed country code).
- R2: Duplicate detection: adding a contact with an existing phone number raises `DuplicateContactError` with the existing contact's name; `merge(other)` exists to combine them.
- R3: `Book`: `add`, `remove`, `find(query)` — partial match on name OR phone OR email; `by_tag(tag)`; `__len__`, `__iter__`, `__contains__(phone_number)`.
- R4: Sort: `sorted(book)` by name, case-insensitive.
- R5: CSV import/export — import must tolerate: missing fields, extra unknown columns (warn, keep), blank lines, duplicate rows (dedupe by phone).
- R6: JSON `save()` / `load()` round-trip.
- R7: `undo()` — the last add/remove/merge is reversible (command stack); `undo` with nothing to undo raises.
- R8: Bad phone number on input → `InvalidPhoneError`, CLI prints a one-line friendly message, exit code 1.
- R9: ≥15 tests including the messy-CSV import test (fixture with 8 rows, 3 dirty).

Exceptions (raise these — all subclass the first one):
- `BookError` — base
- `InvalidPhoneError` — input that can't be normalized to E.164 (matches R8)
- `DuplicateContactError` — add() with an already-existing phone (message names the existing contact, matches R2)
- `ContactNotFoundError` — remove() of an unknown contact
- `NothingToUndoError` — undo() with an empty command stack
- `CsvImportError` — malformed import row (message includes the row number and the problem)

#### Tier 2 - Medium (2–3 weeks each)

**1. Text adventure engine** — a data-driven adventure; the *engine* is the product, the game content is data.

Functional requirements:

- R1: Rooms defined in JSON: `id`, `description`, `exits` (`{"north": "cellar"}`), `items`, `npcs`, `locked_by`.
- R2: Parser handles: `go <dir>`, `take <item>`, `drop <item>`, `look`, `inventory`, `help`, `save`, `load`; unknown verb → "You don't know how to do that" (not a crash).
- R3: **Command pattern**: each verb is a `Command` object with `can_execute(context)` and `execute(context)`; adding a new verb (e.g. `push`) requires touching **one new file only** — OCP, tested.
- R4: Items: pick up, drop, use; a locked door requires holding the matching key; a key that isn't in that room blocks progress (the game must be solvable — a solvability test walks the solution).
- R5: `Player` state (location, inventory, health, turns); `Game` owns the loop and exposes `state` for save/load.
- R6: `save` / `load` full game state to JSON; reloading resumes exactly.
- R7: `Room.from_dict` factory; a bad room JSON raises `ContentError` naming the file and the broken field.
- R8: Tests: full JSON load, scripted playthrough that reaches the win state, unknown-command test, save/load round-trip, solvability walk.

Exceptions (raise these — all subclass the first one):
- `AdventureError` — base
- `ContentError` — a bad room JSON (message names the file and the broken field, matches R7)
- `InvalidCommandError` — a known verb with malformed syntax (`go` with no direction) — note: an *unknown* verb is NOT an error, it's an in-game message (R2)
- `NoExitError` — `go <dir>` where the current room has no exit that way (engine raises; CLI converts to the in-game sentence)
- `CorruptSaveFileError` — load() of a malformed save file

**2. CLI task manager (SQLite)** — a todo app where the schema and layers matter more than the features.

Functional requirements:

- R1: `Task`: id, title, description, `priority` (Enum: LOW/MED/HIGH), `due` (date, optional), `status` (OPEN/DONE/DEADLINE), timestamps.
- R2: Commands: `add`, `list` (filters: `--status`, `--priority`, `--due-today`, `--project`), `done <id>`, `rm <id>`, `edit <id>`.
- R3: Projects: a task belongs to a project; `list --project work`; deleting a project asks (or `--force`).
- R4: **Migrations**: `schema/001_initial.sql`, `002_projects.sql`… applied in order by a hand-rolled `migrate.py` that records applied versions in a table; running it twice is a no-op.
- R5: Custom errors: `TaskNotFoundError`, `ProjectNotFoundError` — CLI turns them into one-line messages + exit code.
- R6: `stats`: counts by project, by status, overdue count, oldest open task.
- R7: **Layers**: `CLI → TaskService → TaskRepository → sqlite3`. The service never imports sqlite3; the repository never imports the CLI. Tests for the service use a `FakeRepository` (dependency-injection payoff).
- R8: ≥20 tests: service-level with the fake repo, repository-level with a temp-file DB, CLI-level via `subprocess` for 3 smoke commands.

Exceptions (raise these — all subclass the first one):
- `TaskManagerError` — base
- `TaskNotFoundError` — an id that doesn't exist (matches R5)
- `ProjectNotFoundError` — an id that doesn't exist (matches R5)
- `InvalidTaskError` — empty title or an unknown priority string
- `InvalidDateError` — a due date that doesn't parse
- `MigrationError` — missing schema file, version applied out of order, or failing SQL (message names the migration)

**3. File organizer CLI** — move files into extension-based folders, safely.

Functional requirements:

- R1: `organize(src)` moves files into subfolders by extension: `*.jpg|jpeg|png|gif` → `Images/`, `*.pdf|doc|txt` → `Documents/`, `*.mp3|wav|flac` → `Music/`, else `Other/`. Mapping is data, not code (a dict you can edit).
- R2: `--dry-run` prints the exact plan (old → new path) and changes nothing; the plan for dry-run and real run must be identical (test asserts this).
- R3: Collision policy, configurable: `suffix` (`report_1.pdf`), `skip`, or `overwrite` (default: suffix).
- R4: `undo` — the last operation log is a JSON file; `undo` restores every original path and removes empty dirs created.
- R5: `--exclude` patterns (`.git`, `node_modules`, hidden files by default) — never traversed.
- R6: `--recursive` (default) vs `--top` (only the top level).
- R7: **Symlinks are never followed** — a test creates a symlink loop and asserts the tool survives and doesn't duplicate files.
- R8: `pathlib` only; zero shell calls; progress bar with a per-file log line.
- R9: ≥15 tests in `tmp_path` fixtures: plan-equality, undo-restores, collision-suffix, exclude-respected, symlink-survival.

Exceptions (raise these — all subclass the first one):
- `OrganizerError` — base
- `PathNotFoundError` — the source directory doesn't exist
- `CollisionError` — target path exists and the collision policy is `fail`
- `NothingToUndoError` — undo with no recorded operation
- `PermissionDeniedError` — wraps OSError/EACCES (message includes the affected path); the tool stops, reports, and never half-moves

**4. Expense tracker + CSV reports** — personal finance with integer-cents discipline.

Functional requirements:

- R1: `Transaction`: amount stored as **integer cents** (never float), category, date, note. A test proves it: `add(0.1) + add(0.2)` totals exactly 13 cents.
- R2: `add`, `list` (`--since`, `--until`, `--category`), `rm <id>` (soft delete into an audit log, not `DELETE`).
- R3: Categories with monthly budgets; `budget` command shows spent / remaining per category and flags overruns.
- R4: Aggregations: total by category, by month, top-5 spenders; all via `sum()` over generators.
- R5: **Messy CSV import**: a real dirty file — mixed date formats (`2026-01-02`, `01/02/2026`, `Feb 2`), a missing field, two duplicate rows, a blank line, a currency symbol in the amount. Import succeeds, reports every quirk it fixed, dedupes.
- R6: Clean CSV export (canonical format only).
- R7: SQLite persistence with a migration file; `report` prints a monthly table + writes `report.json`.
- R8: `dataclass` + `__post_init__`: amount > 0, date valid, category from a known set — violations raise before touching the DB.
- R9: ≥25 tests, including the float-safety test and the full messy-CSV import.

Exceptions (raise these — all subclass the first one):
- `ExpenseError` — base
- `InvalidAmountError` — amount <= 0 or not parseable as money
- `InvalidDateError` — date that fails all supported formats
- `UnknownCategoryError` — a category not in the known set (matches R8)
- `TransactionNotFoundError` — rm / edit of an unknown id
- `CsvImportError` — unrepairable import row (message includes the row number; repairable quirks are fixed and *reported*, not raised)

**5. 2D game with entities & collision** — a top-down grid game where the architecture is the point.

Functional requirements:

- R1: `Entity` base: position, velocity, alive; `Player`, `Enemy`, `Pickup` subclasses with distinct components (health, sprite, AI).
- R2: `rects_overlap(a, b)` AABB collision; per-frame collision resolution: enemy touches player → damage; pickup touches player → collect.
- R3: Enemy AI as a state enum: `WANDER` → `CHASE` (within radius 5) → `ATTACK` (adjacent); states transition on distance + cooldown.
- R4: `World.collide(entities)` uses spatial hashing (a dict of cells) — **not** O(n²); a benchmark test: 200 entities × 1 frame < 5ms headless.
- R5: Wave spawner: wave N spawns N enemies on random edge cells; health/hit-rate scale with N.
- R6: Pickups: health pack, score gem; despawn after 30 ticks; no pickup spawns inside another entity.
- R7: HUD line: score, health, wave; game over screen; restart creates a fresh world with **zero** state leakage (test: two back-to-back sessions, second starts clean).
- R8: Headless API: `World.step()` is pure given a seeded RNG + an input queue — the entire gameplay is testable without a screen.
- R9: Tests: collision unit table (≥8 cases), chase-behavior test, wave-spawn count test, benchmark, no-leak test.

Exceptions (raise these — all subclass the first one):
- `WorldError` — base
- `InvalidSpawnError` — spawning an entity out of bounds or onto an occupied cell
- `MissingComponentError` — an operation needs a component the entity doesn't have (message: entity id + component type)
- `DeadEntityError` — operating on an entity that is no longer alive

**6. Traffic light / vending machine FSM** — a *generic* state machine engine, instantiated twice.

Functional requirements:

- R1: `StateMachine(states, transitions)` where transitions is `{(state, event): next_state}`; `fire(event)` raises `InvalidTransitionError` naming the current state and the legal events.
- R2: Entry/exit hooks per state (callbacks fired on transition); `history()` returns the full state/event log.
- R3: **Traffic light**: `GREEN(30s) → YELLOW(5s) → RED(30s)` loop driven by `tick(dt)`; a pedestrian button event holds the crosswalk green; a test proves the full cycle math (65s per cycle).
- R4: **Vending machine**: insert coin → select product → dispense → refund change; out-of-stock path (refund the selection); `revenue()` report. All money in **integer paise**.
- R5: `render()` prints the state graph (states as boxes, events as arrows) — generated from the transition table, not hand-drawn.
- R6: `save_state()` / `load_state()` — resume both machines mid-flow.
- R7: **Time is injected**: the machines take a `clock` object; tests use a `FakeClock` (no real `sleep` anywhere in the suite).
- R8: Tests: every legal transition, every illegal one, the 65s cycle assertion, vending money math (insert 3 coins, buy 2.55, get 75 paise back — exact).

Exceptions (raise these — all subclass the first one):
- `StateMachineError` — base
- `InvalidTransitionError` — an event that is legal in the table but not in the *current* state; message names the current state and every legal event (matches R1)
- `UnknownEventError` — an event that appears nowhere in the transition table (distinct from InvalidTransitionError — and the message must say so)
- `CorruptStateFileError` — load_state() of a file with an unknown state name
- `Vending-domain: InsufficientCoinsError, OutOfStockError, InvalidSelectionError` — all subclassing StateMachineError

**7. Mini static-site generator** — Markdown in, a website out.

Functional requirements:

- R1: `Site` loads `content/posts/*.md` with front matter (`title`, `date`, `tags`); a post with missing `title` or bad `date` → `SiteBuildError` naming the file + the problem.
- R2: Markdown → HTML (the `markdown` pip package is allowed; keep the parser isolated behind one module).
- R3: **Link rewriting**: `[x](other-post.md)` inside a post becomes `/posts/other-post.html`; broken internal links are a build **error** (listed, not silent).
- R4: Templates: Jinja2 `base.html` + `extends`; header/footer as partials; a category page auto-generated for every tag.
- R5: `build()` emits to `output/`: post pages, index, category pages, `sitemap.xml`, `feed.xml` (valid RSS — tested with an XML parse).
- R6: **Caching**: a second build with no changes rewrites zero files; one changed post rebuilds exactly that post (+ index + category) — the test counts written files and asserts.
- R7: `--watch` (poll-based is fine) rebuilds on change.
- R8: `preview()` starts a local server via `subprocess` and prints the URL.
- R9: Tests: sample 5-post site in `tmp_path` — link rewriting, broken-link failure, category page, sitemap well-formed, cache counts.

Exceptions (raise these — all subclass the first one):
- `SiteBuildError` — base
- `FrontMatterError` — missing title or unparseable date (message names the post file + the field, matches R1)
- `BrokenLinkError` — an internal link to a post that doesn't exist (message names source file and target path, matches R3)
- `TemplateNotFoundError` — a template or partial referenced by `extends` / `{% include %}` is missing

**8. HTTP client library (urllib wrapper)** — a small, opinionated, production-shaped client.

Functional requirements:

- R1: `get(url, headers, timeout)` → `Response(status, headers, body, elapsed_ms, url)`.
- R2: **Retry with exponential backoff + jitter** on 5xx and timeout: `max_retries=3`, base 0.5s; a **test** (fake clock + local server returning 500 twice then 200) proves the delays and the eventual success.
- R3: No retries for non-idempotent methods (POST) by default; `retry_on` is configurable; honors `Retry-After` when present.
- R4: Custom error hierarchy: `NetworkError` → `TimeoutError`, `ConnectionError`, `DNSFailure`; `HTTPError` carries the status + body tail.
- R5: `Client(base_url, default_headers)`; path joining is sane (`/api/v1` + `users/` → one slash, not two).
- R6: **Token-bucket rate limiter** (the one you built in Phase 1!): `RateLimiter(rps)`; a test fires 100 requests at 5 rps and measures they don't exceed the budget.
- R7: **Cache**: in-memory ETag/Last-Modified revalidation; a second `GET` sends `If-None-Match` and stores `304` as a cache hit.
- R8: Request logging: every request (url, status, elapsed) to a pluggable handler; a `ConsoleHandler` prints, a `FileHandler` writes JSON lines.
- R9: Progress callback for bodies > 1MB (chunked reads).
- R10: Tests against a **local `http.server` fixture** (thread, on a random port): retry sequence, cache hit, rate-limit timing, error mapping.

Exceptions (raise these):
- `ClientError` — the base; your CLI / caller catches this one (note the naming: the builtins already own `TimeoutError` and `ConnectionError`, so you must not shadow them)
- `NetworkError` (subclass of `ClientError`)
  - `RequestTimeoutError` — a single attempt exceeded its timeout (retried, then raised)
  - `ConnectionFailureError` — refused / reset / unreachable
  - `DNSFailureError` — the host doesn't resolve
- `HTTPError` (subclass of `ClientError`) — any non-2xx after the retry policy is exhausted; carries status + body tail
  - `ServerError` — a 5xx that survived `max_retries`
  - `RateLimitedError` — a 429 that survived the token budget + `Retry-After`
- `CacheError` — a corrupt local cache entry (cache entry is discarded, request retried clean)

#### Tier 3 - Hard (1 month each)

**1. Expression interpreter** — a real mini-language: lexer → parser → AST → evaluator.

Functional requirements:

- R1: **Lexer**: tokens `NUM`, `IDENT`, `OP(+,-,*,/,%,^,=)`, `LPAREN`, `RPAREN`; skips whitespace; a malformed input raises `LexError` with position (char + line).
- R2: **Grammar** (recursive descent): `expr → term (('+'|'-') term)*`, `term → factor (('*'|'/') factor)*`, `factor → NUMBER | IDENT | '(' expr ')' | '-' factor`; precedence is structural, not a table hack.
- R3: **Parser** → AST: dataclass per node type (`NumNode`, `VarNode`, `BinOpNode`, `CallNode`) with clean `__repr__`.
- R4: **Evaluator**: runs the AST against a scope dict; supports `let x = ...`, user functions (`fn f(x) = x*x`), and calls.
- R5: **REPL**: prompt, `:history`, `:quit`; error for an undefined variable shows the name + line; `interp.py program.ex` runs batch mode.
- R6: Typed errors: `SyntaxError` (with an underlined snippet), `UndefinedVarError`, `DivZeroError`, `ArityError` (wrong arg count) — all with the expression that caused them.
- R7: Numbers: float arithmetic with integer display when the value is integral (`4.0` prints as `4`).
- R8: **40+ tests**: precedence table (`2+3*4=14`, `2*3+4*5=26`), parenthesization, assignment + scope, function recursion (factorial(5)=120), every error type with its message.
- R9: Stretch (do if early): comparison operators (`>`, `==`), string literals, `mod`.

Exceptions (raise these — all subclass the first one):
- `InterpretError` — base for all interpreter failures
- `LexError` — with character + line position (matches R1)
  - `UnexpectedCharError` — a character the lexer can't classify
- `ParseError` — structural failure; note the deliberate name: you do NOT shadow the builtin `SyntaxError` (that's a lesson, put it in the docstring)
- `UndefinedVarError` — an identifier never bound (message: name + line)
- `DivZeroError` — division by zero at eval time
- `ArityError` — calling a function with the wrong argument count (message: name, expected, got)
- `TypeMismatchError` — if you do the string stretch: `1 + "a"`

**2. Tiny key-value store on disk** — a persistent KV with crash recovery and a CLI.

Functional requirements:

- R1: Python API: `set(key, value)`, `get(key)`, `delete(key)`, `keys(prefix)`, `len(store)`; `__getitem__` / `__setitem__` / `__delitem__` / `__contains__` / `__iter__`.
- R2: **Persistence model**: an append-only `journal.log` (key, op, value-hash, timestamp, CRC) + periodic `snapshot.dat`. Writes go to the journal **first**.
- R3: **Crash recovery on startup**: replay the journal over the last snapshot; a torn (truncated) final record is detected by CRC and cleanly discarded. **Test:** write 1000 keys, kill the process mid-write (test spawns and kills a child), restart, assert the last 1000−k keys are intact and k is computable.
- R4: `compact()`: writes a new snapshot, truncates the journal; a `bench` command reports ops/sec for 10k ops (with and without auto-compaction).
- R5: Atomic file writes: write to a temp file + `os.replace`, never in-place.
- R6: CLI: `kv.py set k v`, `get k`, `del k`, `scan prefix`, `compact`, `bench`, `stats` (journal size, snapshot age, key count).
- R7: Keys: UTF-8 bytes, max 1KB; values: arbitrary bytes, max 1MB; oversize → `TooLargeError`.
- R8: `open()` is idempotent-safe: two handles on one store in the same process share a lock (one deliberate test corrupts this and expects a clean `LockBusyError`).
- R9: ≥25 tests including the kill-the-process crash test and a 10k-key fuzz round-trip.

Exceptions (raise these — all subclass the first one):
- `StoreError` — base
- `TooLargeError` — key > 1KB or value > 1MB (message says which one and the actual size, matches R7)
- `LockBusyError` — a second handle opened on the same store in the same process (matches R8)
- `CorruptRecordError` — a torn journal record found during recovery (recovery path: discard + count, don't crash)
- `NoRecoveryDataError` — no readable snapshot AND an empty or unusable journal: nothing to recover
- `SnapshotError` — the snapshot write / compact step failed mid-operation

**3. Mini Redis** — a TCP server speaking RESP, in-memory, single-node.

Functional requirements:

- R1: **RESP protocol**: parse all 5 types (simple string, error, integer, bulk, array); write all 5; a unit test table covers valid + malformed input (half-read bulk, wrong arity, oversize bulk).
- R2: Commands: `PING`, `SET k v [EX s]`, `GET`, `DEL`, `KEYS pattern` (glob), `INCR`, `EXPIRE`, `TTL`, `DBSIZE`.
- R3: **Expiry**: lazy check on access + a periodic sweep task; a test sets `EX 1`, sleeps 1.1s, asserts `GET` → nil.
- R4: **Concurrency**: `asyncio` server; `bench` client does 1000 `INCR`s from 100 concurrent clients → the key is exactly 1000 (tests event-loop safety, not threads).
- R5: Error handling in RESP format: wrong arity → `ERR wrong number of arguments`; `INCR` on a non-integer → `ERR value is not an integer`.
- R6: Structured logging: every command logged as JSON (`conn`, `cmd`, `args`, `ms`) to stdout; a `--quiet` flag suppresses.
- R7: `--snapshot file`: save state on clean shutdown, restore on startup; a corrupt snapshot → clear `SnapShotError` + exit 1, never a half-loaded state.
- R8: Graceful shutdown: `SIGINT` → finish in-flight commands, snapshot, close listeners, exit 0.
- R9: **No external deps** beyond the stdlib (`asyncio`, `socket`); the RESP parser is a standalone testable module.
- R10: ≥20 tests: protocol table, command semantics, concurrency bench, expiry, snapshot round-trip.

Exceptions — the teaching point of this project is that there are **three classes of error**, and you must document which is which:
- **Client-facing** (returned to the client as a RESP `-ERR` string; the connection stays open): wrong arity, `INCR` on a non-integer, unknown command. These are produced by an internal `CommandError` — and a test proves they never leak out as a traceback.
- **Connection-killing** (close *that socket only*; the server keeps running): unparseable protocol garbage from a client — a `ProtocolViolationError` caught at the connection level.
- **Server-killing** (fatal, exit 1): `SnapshotCorruptError` on startup, `PortInUseError` on bind. A test proves a crashing client connection never takes the server down.

**4. Async web crawler** — a polite concurrent crawler with a real pipeline.

Functional requirements:

- R1: `Crawler(seed_urls, max_pages, max_depth)` — BFS crawl; depth and page caps are hard stops.
- R2: **Domain allow-list**: only URLs whose host matches a seed host (or a configured allow-list) are enqueued; absolute URL parsing from relative links (tests: `/a/b`, `//host/x`, `mailto:`, `javascript:`, `#frag`).
- R3: **Politeness**: per-domain `asyncio.Semaphore(2)`, configurable `min_delay` between requests per domain, `robots.txt` parsed and honored (a real robots test with a local server serving one).
- R4: **Dedup**: URL normalization (lowercase host, strip fragment, sorted query params, strip `utm_*` params) into a visited set; `scan`/`dry-run` prints what *would* be crawled.
- R5: **Pipeline with backpressure**: `fetch → parse → queue` as `asyncio.Queue(maxsize=N)`; producer blocks when the queue is full — a test proves the max size is never exceeded.
- R6: **Retry**: 429/5xx → backoff honoring `Retry-After`; permanent 4xx → skipped and logged, not raised.
- R7: **Output**: JSON Lines (`url`, `status`, `title`, `links`, `bytes`, `ms`, `ts`); a `report()` summary: pages ok/failed, per-domain breakdown, top-5 slowest.
- R8: **Graceful cancel**: `Ctrl+C` → in-flight tasks finish, the queue is drained, the report is printed, exit code 130.
- R9: `User-Agent` identifies the crawler with a fake contact (documented in README); no crawling of third-party domains you don't own without asking.
- R10: Tests use a **fake transport** (monkeypatched fetch returning canned responses): dedup, domain filter, robots obey, backpressure count, retry timing, cancel-doesn't-lose-already-fetched.

Exceptions (raise these — all subclass the first one):
- `CrawlerError` — base
- `SeedError` — zero valid seed URLs after normalization + robots check
- `RequestTimeoutError` — one URL exceeded its timeout (retried with backoff, then the page is skipped + logged)
- `TransientHttpError` — a 429/5xx that survived all retries (page skipped, logged — never raised out of the crawl)
- `PermanentHttpError` — a 4xx that will never succeed (skipped, logged)
- `UnparseablePageError` — bytes that decode to nothing usable as HTML
- `OutputWriteError` — the JSON Lines sink failed
- `The policy: crawl failures are logged and skipped. A single bad page never kills the crawl` — and a test proves the crawl finishes after N bad pages.

**5. ECS game engine** — a mini entity-component-system where *entities are just IDs*.

Functional requirements:

- R1: `Entity` = an integer id. `Component` = plain data (`Position(x,y)`, `Velocity(dx,dy)`, `Health(max,cur)`, `Sprite(char)`).
- R2: `World`: `spawn()` → id; `add_component(id, comp)`, `get_component(id, type)`, `remove_entity(id)`; `entities_with(*types)` → the set of ids having all of them.
- R3: `System` = a callable `(world, dt) -> None`; the **scheduler** runs systems in a fixed, user-declared order each frame; reordering the list changes behaviour (test: movement-before-damage vs damage-before-movement on a dying entity).
- R4: Built-in systems: `MovementSystem` (`pos += vel*dt`), `DamageSystem` (a "poison" component ticks health), `RenderSystem` (sprite chars onto a terminal grid).
- R5: **Fixed timestep**: an accumulator loop simulates in 60Hz steps regardless of wall-clock; `--headless` runs N steps per second for tests.
- R6: `spawn_player()`, `spawn_enemy()` factories; a combat system applies damage on collision between `Sprite`-ed entities with opposing `Team` components.
- R7: **OCP proof**: add a new behaviour ("shield: negates the next hit") by adding **one new component file + one new system file** and zero edits to existing systems — a test spawns a shielded enemy and asserts.
- R8: `debug()` prints entity count, per-component counts, per-system ms; a benchmark: 1000 entities × 60 steps < 2s headless.
- R9: **No entity classes**: the README shows the contrast — the same 5 behaviours in the Tier 2 style would need ≥8 classes; ECS needs 0 entity subclasses.
- R10: Tests: pure system math (movement in N steps = exact position), scheduler order, removal-doesn't-leak (GC of components), OCP test, benchmark.

Exceptions (raise these — all subclass the first one):
- `EngineError` — base
- `UnknownEntityError` — any operation on an id that was removed (message: the id)
- `MissingComponentError` — get_component / add_component for a type the entity doesn't have / shouldn't get twice (message: id + component type)
- `InvalidSystemError` — a registered system that isn't callable or has the wrong signature (caught at registration, not mid-frame)
- `SystemCrashError` — a system raised during a frame: the engine catches it, reports it, and the frame continues (document this decision — a crashing system must not kill the simulation)

**6. Plugin system** — a host application that loads and isolates third-party plugins.

Functional requirements:

- R1: A plugin is a package exposing `class Plugin` with `name()`, `version()`, `register(api)`.
- R2: The host scans `plugins/` at startup via `importlib`; a plugin that fails to import is **skipped with a warning** (logged, never fatal).
- R3: **API object**: the only thing a plugin gets: `store` (KV), `bus` (pub/sub), `http` (client), `log`. The host's internals are not importable; a test proves a plugin can't reach `os`/`subprocess` through the API surface (document the real limits honestly — Python isn't a jail).
- R4: **Event bus**: `bus.publish("topic", payload)` → all subscribers for `topic`; a crashing subscriber is caught, logged, and its errors counted in `stats()` — other subscribers still fire (isolation test).
- R5: **Version gate**: host requires plugin API `>=1.0, <2.0`; a v2 plugin is skipped with a clear log line, not an `AttributeError` traceback.
- R6: `pluginctl` CLI: `list` (name, version, enabled, last-error), `enable`, `disable`, `inspect <name>` (its bus topics, its store keys).
- R7: Disable list persisted; `enable` of a disabled plugin re-runs `register` with a fresh API.
- R8: **Three sample plugins**: `logger_plugin` (writes events to a file), `echo_plugin` (re-publishes), `failing_plugin` (raises in a subscriber) — the host stays up through a stress test of 100 publishes.
- R9: Deterministic load order: plugins load in name-sorted order; `register` order documented.
- R10: ≥20 tests: discovery, import-failure isolation, version gate, crash isolation, stats counting, disable/re-enable, sample plugins end-to-end.

Exceptions (raise these — all subclass the first one):
- `HostError` — base
- `PluginLoadError` — import failed for a plugin (captured per plugin, stored, shown by `pluginctl list`; never fatal — matches R2)
- `PluginVersionError` — the API version gate failed (matches R5: a log line, not a traceback)
- `PluginRegisterError` — a plugin's register() raised (plugin marked disabled, host continues)
- `UnknownPluginError` — enable / disable / inspect of a name that isn't loaded
- `SubscriberError` — wraps a crashing bus subscriber's exception (carries the original; counted in stats() — matches R4)

**Phase 2 Exit Gate:**
- [ ] Tier 1 complete (all 10 projects)
- [ ] Tier 2: at least 4 (the FSM and the task manager are strongly recommended — they feed Phases 4 & 5)
- [ ] Tier 3: at least 2
- [ ] Every project meets **≥80% of its own R-list**; the rest are documented as known gaps in its README
- [ ] Every project has a README (design + decisions + how to run) and a `pytest` suite with **>80% coverage** that runs under 30 seconds
- [ ] All 15 OOP rungs have their toy + NOTES entry, and you can, from memory, name where each pattern lives in one of your projects

---

## Phase 3 - Linux & the Terminal

> **This phase is 100% debugging-oriented.** No shell scripting. Learn the commands you reach for when production is on fire.

> **macOS note (critical):** BSD userland ≠ GNU userland. Many tutorials give Linux flags that error on your Mac.
> | Task | macOS | Linux (GNU) |
> |---|---|---|
> | recursive size | `du -sh .` | `du -sh .` |
> | show open files | `lsof -i :8080` | `ss -tlnp` |
> | DNS | `dig`, `host` | same |
> | listening ports | `lsof -i -P -n` | `ss -tulnp` |
> | process tree | `pstree` (install) or `ps` | `pstree` |
> | trace a syscall | `dtruss` (needs sudo) | `strace` |
> | color output | `grep --color` ✓ | same |
> | follow logs | `tail -F` | `tail -F` |
>
> **Get a Linux box in Phase 0.** Do these exercises on both so the differences stop surprising you.

### The command set (memorize these, ~70 commands)

**Navigate & inspect**
`pwd` `ls` (`-l` `-a` `-h` `-t`) `cd` `mkdir` `-p` `touch` `cp` `mv` `rm` `-r` `-i` `find` `tree` `file` `stat` `du` `df` `du -sh` `realpath` `readlink`

**Read & search**
`cat` `less` `head` `tail` `-f`/`-F` `wc` `grep` (`-i` `-r` `-n` `-v` `-c` `-E` `-w`) `rg` (ripgrep - learn this, it's 10× faster) `sort` (`-n` `-u`) `uniq` `-c` `cut` `-d` `tr` `sed` (`s///g`, `-n`, `q`) `awk` basics (`{print $1, $NF}`, `NR`) `column` `jq`

**Permissions & identity**
`whoami` `id` `groups` `sudo` `su` `chmod` (`-R`) `chown` `chgrp` `umask` `ls -l` field meanings

**Processes - the debugging core**
`ps` (`aux`, `-ef`, `--forest`) `top` `htop` `kill` (-9, -TERM) `pkill` `pgrep` `jobs` `fg` `bg` `wait` `nohup` `disown` `lsof` `time` `strace`/`dtruss` `/proc` `kill -l`

**System & resources**
`uname` `-a` `hostname` `uptime` `free`/`vm_stat` `top` `dmesg` `sysctl` `env` `printenv` `export` `PATH` `nproc` `date`

**Logs & services (Linux)**
`systemctl status` `journalctl` (`-f` `-u` `--since`) `service` `crontab -l` `ps aux` triage

**Networking - absolutely essential**
`ping` `curl` (`-v`, `-I`, `-X`, `-d`, `--resolve`, `-w`) `wget` `dig` `+short`, `nslookup` `host` `nc` / `netcat` `telnet` `ip addr` `ip route` `ifconfig` `ss` `-tlnp` `netstat` `traceroute` `mtr` `arp`

**Transfer & archive**
`scp` `rsync` (`-avz`, `--delete`, `--exclude`) `ssh` (keys, `-L`, `-R`, port forwarding, `~/.ssh/config`) `tar` (`-czf`, `-xzf`) `gzip` `zip` `unzip`

**Shell mechanics you must own**
Pipes `|` `>` `>>` `2>` `2>&1` `tee` `xargs` `&&` `||` `;` backticks vs `$()` here-docs `<<EOF` subshell `( )` grouping `{ }` brace expansion `{1..10}` `~` expansion globbing `*` `?` `[a-z]` quoting `'...'` vs `"..."` (why `$HOME` works in one and not the other) process substitution `<(...)` `$(cmd)` exit codes `$?` `set -e` `set -x` traps `SIGINT` `Ctrl-C` vs `Ctrl-\`

**Config & environment**
`~/.zshrc` / `~/.bashrc` - aliases, `PATH`, `EDITOR`. Learn `alias`, `export`, `history`, `Ctrl-R` reverse search, `!!`, `!$`.

### Exercises

1. Find the 10 largest files in a directory tree
2. Find all files modified in the last hour
3. Count lines of code in a repo, excluding vendored dirs
4. Find every `.py` file that imports a given module
5. Tail a log file and filter for `ERROR` as it streams
6. Find what's listening on port 8080, and which process owns it
7. Kill a hung process politely, then forcefully
8. Start a process, background it, nohup it, then find and kill it
9. Transfer a directory between two machines with `rsync`, twice, efficiently
10. Write a log-rotation alias using `tail -F | grep`
11. Diagnose a high-CPU process using `top` → `strace` → `/proc/<pid>`
12. Use `curl -w` to benchmark 3 API endpoints and find the slowest
13. `dig` your way from your domain down to a specific A record; explain each hop
14. Use `nc` to test what a server does when you send garbage bytes
15. Set up `~/.ssh/config` with a short alias and key-based login

### Deliverable: `debugging-playbook.md`

Your personal runbook. As you solve each issue in later phases, append the exact command sequence that solved it. By Phase 7 this will be your single most valuable file.

**Exit gate:** someone hands you "the API is down" and you can, in under 5 minutes, tell them whether it's the process, the port, the network, or the disk - **without touching the code**.

---

## Phase 4 - OS, Processes, Databases & Networking (practical)

> Everything here is taught by **building the thing and breaking it**. No lecture-only sections.

### 4A - How the OS works (because you're already a user of it)

| Concept | Practical angle |
|---|---|
| Process vs thread | Why a CPU-bound Python task stalls your API |
| `fork` / `exec` / `spawn` | What `subprocess.Popen` actually does |
| PID, PPID, zombie, orphan | Processes you can't kill; `ps -ef` forensics |
| Virtual memory & paging | Why 40 subprocesses OOM your laptop |
| Stack vs heap | Why recursion blows up, why you get memory errors |
| File descriptors | The real cost of not closing files; `ulimit -n` |
| Scheduling & context switch | Why `time.sleep` in an async handler is catastrophic |
| Signals | `SIGTERM` vs `SIGKILL`; graceful shutdown |
| Syscalls | The boundary between your code and the kernel |
| `mmap`, page cache | Why the second read is faster |

**Build these:**
1. `my_shell.py` - spawn a shell, pipe a command, read stdout, read stderr separately
2. `process_pool.py` - fork N workers, distribute work, collect results, reap zombies correctly
3. `tail_f.py` - reimplement `tail -F` in Python (reopen the file when rotated)
4. `top_clone.py` - live system monitor: CPU, memory, per-process stats, refresh
5. `mini_shutdown.py` - trap `SIGINT`/`SIGTERM`, flush state, exit cleanly
6. **Benchmarks:** compare `threading` vs `multiprocessing` vs `asyncio` for (a) HTTP requests, (b) CPU-heavy math, (c) file IO. Write down *when each wins.*

### 4B - Concurrency in Python (do this properly)

- `threading` + `Lock` + `Queue`; the GIL and what it does/doesn't protect
- `multiprocessing` + `Pool` + IPC cost
- `asyncio`: event loop, coroutines, `await`, `gather`, `create_task`, `TaskGroup`, cancellation, `queue`, `to_thread`
- **The #1 async sin:** calling a blocking function in a coroutine. Prove it with a latency graph.
- Write a concurrency matrix table and keep it in your notes.

### 4C - Databases (practical)

**Start with SQLite** - zero install, real SQL, real transactions.

| Topic | Must-do |
|---|---|
| CRUD | `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`, `WHERE`, `ORDER BY`, `LIMIT` |
| Joins | `INNER`, `LEFT`, `RIGHT`, `FULL OUTER` (in Postgres), self-joins |
| Aggregation | `GROUP BY`, `HAVING`, `COUNT/SUM/AVG/MIN/MAX`, `COUNT(DISTINCT)` |
| Subqueries | Scalar, `IN`, `EXISTS`, correlated - and why `EXISTS` beats `IN` on big data |
| Windows | `ROW_NUMBER()`, `RANK()`, `LAG()`, `SUM() OVER` |
| Constraints | `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, `CHECK` |
| Transactions | `BEGIN/COMMIT/ROLLBACK`, isolation levels, what partial writes do |
| Indexes | `CREATE INDEX`, B-tree intuition, composite indexes, **when indexes make writes slower** |
| Query plans | `EXPLAIN QUERY PLAN`. Find the N+1. |
| Normalization | 1NF→3NF, denormalization trade-offs, why NoSQL repeats data |
| Modeling | Entities, relationships, cardinalities, soft deletes, `created_at`/`updated_at` |

**Then PostgreSQL:** `psql`, indexes, `EXPLAIN ANALYZE`, JSONB, CTEs, window functions, connection pooling, migrations.

**Then Redis:** data structures (string, hash, list, set, zset), TTL, `INCR` (rate limiter!), `LPUSH/BRPOP` (queue!), pub/sub.

**Then ORM:** SQLAlchemy 2.x Core, then ORM, then Alembic migrations. Understand the N+1 problem it can cause.

**Build:**
1. Library management system - full CRUD, joins, reports
2. Add indexes, measure the before/after with `EXPLAIN`
3. A migration from v1 to v2 schema via Alembic
4. A rate limiter backed by `INCR` + `EXPIRE` in Redis
5. A job queue: `LPUSH` producer, `BRPOP` consumer, with retries and a dead-letter list

### 4D - Networking (build it, don't read it)

| Concept | Build it |
|---|---|
| OSI/TCP/IP layers | Trace a real request with `tcpdump`/DevTools and identify each |
| IP addressing, subnetting | Design subnets for a 3-tier app |
| TCP handshake | Build `tcp_server.py` / `tcp_client.py` with raw sockets; see SYN/ACK in `tcpdump` |
| Sockets & `bind`/`listen`/`accept` | Your own HTTP server (see below) |
| UDP vs TCP | Write a UDP "speed test" and compare loss |
| DNS in depth | `dig` every record type; write a DNS query in raw bytes |
| DHCP | Read what it does; document the DORA process |
| NAT & port forwarding | Run a service on your LAN and reach it from your phone |
| TLS/SSL | `openssl s_client -connect host:443`, read the cert chain by hand |
| HTTP/1.1 vs HTTP/2 | Compare with DevTools + `curl -w` |
| Firewalls | Why your port is unreachable from outside |
| Latency & bandwidth | Measure RTT to 5 hosts; plot it |
| Load balancing | Round-robin vs least-connections, write both in 30 lines |

**Build (hard mode):**
1. **HTTP server from scratch** using `socket` only - parse the request line, headers, and body. No frameworks. Serve HTML.
2. Raw DNS query encoder/decoder (build a query, parse A records)
3. WebSocket handshake from scratch (`Sec-WebSocket-Key` + magic GUID + SHA1 + base64)
4. A TCP chat server with threads (Phase 2 mini-Redis follow-up)
5. A localhost-only port scanner - **only your own machine, only to learn**, never a network you don't own
6. A reverse proxy in front of your FastAPI app

### 4E - Logging (make this excellent - it's your career)

- `logging` module properly: levels, **never** `print()` in a service
- Root logger vs named loggers, `basicConfig`, propagation
- Formatters: timestamps, levels, module/line, **structured JSON logs**
- Handlers: console, file, rotating (`RotatingFileHandler`), syslog, HTTP
- **Context:** `LoggerAdapter`, `contextvars`, correlation/request IDs so a request can be traced across lines
- Log levels as policy: what goes where, and why `ERROR` isn't for expected failures
- Sanitization: **never log passwords, tokens, or PII**
- Logging in async code (the classic interleaving bug)
- Reading logs during an incident: `--since`, filtering, `grep` + `awk` pivots

### 4F - The debugging playbook (this phase is the point)

```
Symptom → Is the process alive?     ps aux | grep X
       → Is it listening?          lsof -i :PORT / ss -tlnp
       → Does the port route?      curl -v http://localhost:PORT
       → Is DNS resolving?         dig +short HOST
       → What does the log say?    tail -F app.log | grep -i error
       → What are its fds?         lsof -p PID
       → What syscalls is it in?   strace -p PID (Linux) / dtruss (macOS)
       → Is it OOM/thrashing?      top / vm_stat / dmesg
       → Is the disk full?         df -h / du -sh /path
       → What changed?             git log --since="2h ago"
```

Also learn: `pdb` (`b`, `c`, `n`, `s`, `l`, `p x`, `w`, `pp`), `breakpoint()`,
`pdb.post_mortem()`, reading a traceback bottom-up, and `import pdb; pdb.set_trace()`.

**Projects for this phase (playful → serious):**

| Level | Project | Teaches |
|---|---|---|
| Playful | Log tailer with live filtering | `tail -F` from scratch |
| Playful | System monitor | Reading `/proc` |
| Playful | Threaded TCP chat | Sockets + concurrency |
| Playful | HTTP server from scratch | The actual protocol |
| Medium | Async URL checker (1,000 URLs, concurrency tuning) | asyncio + backpressure + timeout tuning |
| Medium | Mini database engine (LSM or B-tree on files) | Storage internals |
| Medium | Redis clone (subset of RESP) | Protocols + data structures |
| Medium | Web scraper with a real pipeline | HTTP, HTML parsing, rate limits, error handling |
| Serious | **Observability service**: instrument a FastAPI app with structured logs, request IDs, `/metrics`, and a dashboard | Production engineering |
| Serious | **Multi-service system**: API + worker + Postgres + Redis + Docker Compose, with a kill-switch chaos test | Everything |

**Phase 4 Exit gate:**
- [ ] 8+ projects shipped, including 2 in the "serious" row
- [ ] Can explain, with a whiteboard, how a TCP connection is established
- [ ] Can read an `EXPLAIN` plan and fix an N+1
- [ ] Every project has structured logging and a test suite
- [ ] `debugging-playbook.md` has 15+ real entries
- [ ] You have personally debugged at least one issue to root-cause using only terminal commands

---

## Phase 5 - The Web End to End + FastAPI

### Part A - What happens when you type `www.xxxxx.com`

**Do this twice: first read it, then reproduce every step on your own machine.**

1. **Browser** - parses input, checks HSTS preload list, checks `hosts` file, checks DNS cache, checks `/etc/hosts`
2. **URL parsing** - scheme, host, port, path, query, fragment
3. **DNS resolution**
   - Ask the resolver (from `/etc/resolv.conf`) over UDP:53
   - Resolver checks its cache (respecting TTL)
   - On a miss: root servers (`.`) → TLD servers (`.com`) → authoritative nameservers
   - Records involved: `A`, `AAAA`, `CNAME`, `NS`, `MX`, `TXT`, `SOA`
   - **Do it yourself:** `dig www.google.com +trace` and explain every hop
4. **Route selection & TCP handshake**
   - Subnet + routing table → next hop → ARP → MAC
   - `SYN` → `SYN-ACK` → `ACK` (see it in `tcpdump`)
   - QUIC/UDP alternative (HTTP/3) - know it exists
5. **TLS handshake (TLS 1.3)**
   - `ClientHello` (SNI! ALPN! ciphers, key share)
   - `ServerHello`, **certificate chain**, OCSP stapling
   - Key exchange (ECDHE) → session keys → `Finished`
   - **Do it yourself:** `openssl s_client -connect www.xxxxx.com:443 -servername www.xxxxx.com`
6. **HTTP request** - method, path, version, headers (`Host`, `User-Agent`, `Accept`, `Cookie`), body
7. **The server side** (your app's world)
   - CDN / Anycast edge → reverse proxy (nginx) → load balancer → your server
   - Process model (uvicorn/gunicorn workers), routing, middleware chain
   - Business logic, database, cache
   - Response: status, headers, body
8. **Browser rendering pipeline**
   - Parse HTML → DOM → parse CSS → CSSOM → Render tree → Layout → Paint → Composite
   - Blocking vs non-blocking resources, reflows, `content-visibility`
   - **Do it yourself:** open DevTools → Network → enable a waterfall view; trace one request
9. **After the response** - connection reuse (keep-alive), connection close, TLS session resumption, caching

**Deliverable:** `web-request-journey.md` - a diagram plus terminal commands demonstrating each of the 9 steps for a domain you choose. This document is a genuine interview differentiator.

### Part B - HTTP properly (the protocol as an engineer)

- Methods: `GET POST PUT PATCH DELETE HEAD OPTIONS TRACE`; **idempotency & safety**
- Status codes: 1xx→5xx, and which ones you actually return
- Headers: `Host`, `Content-Type`, `Content-Length`, `Accept`, `Authorization`, `Cache-Control`, `ETag`, `Vary`, `X-Forwarded-*`
- **Caching** - `Cache-Control` directives, `ETag`/`If-None-Match`, revalidation, CDN caching, why you need a cache-busting strategy after deploys
- **Cookies & sessions** - `Set-Cookie`, `HttpOnly`, `Secure`, `SameSite`, signed cookies, JWT vs session
- **CORS** - why it exists, what a preflight `OPTIONS` is, why it breaks
- Content negotiation, `multipart/form-data`, chunked transfer encoding, compression (`gzip`/`br`)
- Keep-alive, pipelining, HTTP/2 multiplexing, HTTP/3
- WebSockets (full-duplex) vs SSE vs long-polling
- REST resource design, pagination (cursor vs offset), filtering, versioning strategies
- GraphQL & gRPC: what problem each solves, when it's worth it
- Idempotency keys, optimistic concurrency, ETags for `PUT`

### Part C - Python async deep dive (do this *before* FastAPI)

FastAPI is only as good as your async understanding.

- Event loop internals: `select`/`epoll`/`kqueue`
- `async def` vs `def` in a web framework - **when each is correct**
- `await`, `asyncio.sleep` vs `time.sleep`
- `asyncio.gather`, `TaskGroup`, semaphores, `asyncio.Queue`
- **Blocking the loop** - write a demo that adds 10s of latency, then fix it with `asyncio.to_thread` / a threadpool
- Timeouts (`asyncio.timeout`) and cancellation semantics
- Connection pooling for HTTP clients (`httpx.AsyncClient`)
- Measure everything with a load generator

### Part D - FastAPI, properly

| Topic | Detail |
|---|---|
| Project structure | `app/main.py`, routers, dependencies, config, services, repositories |
| Pydantic v2 | models, validators, `Field`, settings, serialization |
| Routing | `APIRouter`, path/query params, response models, status codes |
| Dependency injection | `Depends`, `yield` dependencies for cleanup, dependency caching |
| Middleware | custom middleware, CORS, request-ID middleware, timing middleware |
| Lifespan | startup/shutdown, connection pool warmup, graceful shutdown |
| Async DB | async SQLAlchemy / asyncpg, sessions, transactions per request |
| Auth | OAuth2 + JWT, password hashing (`argon2`/`bcrypt`), refresh tokens, RBAC |
| Errors | `HTTPException`, custom exception classes, global handlers, RFC 7807-style errors |
| Validation | request validation, response validation, and what happens when it fails |
| Testing | `pytest` + `httpx.AsyncClient` + `TestClient`, fixtures, DB fixtures |
| Docs | OpenAPI/Swagger, which docs to expose in prod (or not) |
| Performance | `uvicorn` workers, `gunicorn` config, async vs sync routes, profiling (`py-spy`) |
| Background work | `BackgroundTasks`, Celery/RQ/arq, when a queue is mandatory |

### Part E - Phase 5 projects (playful → serious)

| Level | Project | Teaches |
|---|---|---|
| Playful | "What is my IP" service | Request/response, external call, timeouts |
| Playful | URL shortener | Schema design, collisions, redirects |
| Playful | Markdown → HTML API | Parsing, content types, input validation |
| Playful | Webhook receiver + inspector | Payload handling, retries, replay |
| Medium | Pastebin (expiring links) | TTL, storage, caching |
| Medium | Blog API with auth + RBAC | JWT, hashing, migrations, permissions |
| Medium | Real-time chat (WebSockets) | Connection lifecycle, broadcast, backpressure |
| Medium | Rate-limited public API | Token bucket, Redis, headers, 429s |
| Medium | File upload service | Streaming, size limits, content sniffing |
| Medium | Async scraper API | Task queues, concurrency limits, politeness |
| Serious | **Mini search engine** | Inverted index, tokenizer, ranking, pagination |
| Serious | **Notification fanout service** | Queues, dedup, rate limits, delivery retries |
| Serious | **Multi-tenant API gateway** | Auth, quotas, routing, observability |
| Serious | **Realtime collaborative editor** (CRDT-lite) | Concurrency, conflicts, websockets, persistence |

**Phase 5 Exit Gate:**
- [ ] `web-request-journey.md` complete, with reproducible commands
- [ ] `openssl s_client` output explained line by line
- [ ] Can explain CORS from memory, including the preflight
- [ ] Async vs sync route decision made correctly in your own code
- [ ] 5+ FastAPI projects, ≥1 "serious"
- [ ] One app deployed publicly with TLS and monitoring

---

## Phase 6 - Containers, Deployment & Pipelines

> Goal: push to `main` → a URL changes. That's the milestone.

### Part A - Containers

- **Why containers** - the "it works on my machine" problem, precisely
- Images vs containers vs volumes vs registries (the vocabulary everyone muddles)
- Layers, caching, why image size explodes and how to keep it small
- **Dockerfile, done right:** pinned base images, non-root user, multi-stage builds, `.dockerignore`, layer ordering for cache hits, `HEALTHCHECK`
- `docker compose` for a real multi-service stack (app + db + redis + proxy)
- Volumes vs bind mounts, networks, port mapping
- Resource limits (`--memory`, `--cpus`), restart policies
- Container security: minimal images, no secrets in layers, read-only rootfs, scan with `trivy`
- Alternative runtimes: understand that containers are just namespaces + cgroups (Linux) and that **macOS runs them in a VM** (this is *why* bind-mount performance is different)

### Part B - Orchestration (enough to be dangerous)

- Why compose isn't enough at scale
- Kubernetes core objects: **Pod, Deployment, Service, Ingress, ConfigMap, Secret**
- Probes (liveness/readiness/startup), resource requests/limits, rolling updates
- Try it locally: `kind` or `minikube`. Deploy your FastAPI app + Postgres.
- Helm charts: read one, then write one
- Managed alternatives: Fly.io, Render, Railway, App Runner, Cloud Run - **use one of these for your first deploy** (10 minutes vs 10 hours)

### Part C - CI/CD

**Write this pipeline and make it real:**

```
push / PR
  → lint (ruff) + format check
  → type check (mypy)
  → unit tests + coverage gate
  → integration tests (docker-compose services)
  → build Docker image (layer-cached, tagged with git SHA)
  → security scan (pip-audit + trivy)
  → push image to registry
  → deploy to staging (auto)
  → smoke tests against staging
  → manual approval gate
  → deploy to production
  → health check + smoke tests
  → notify (Slack/Discord) + rollback on failure
```

Learn: **artifacts vs rebuilds**, **matrix builds**, **caching strategies**, **secrets management in CI**, **environments & approvals**, **semantic versioning & tags**, **zero-downtime deploys** (rolling, blue/green, canary), **rollback strategy**.

Also: trunk-based development, PR review culture, conventional commits.

### Part D - Infrastructure as code (introduction)

- Terraform basics: providers, resources, variables, state, plan/apply, drift
- Write Terraform for: a VM, a container registry, a managed DB
- Cost awareness: everything you deploy costs money; tag and delete resources

### Part E - Observability & reliability in prod

- **Metrics** (Prometheus + Grafana): RED method (Rate, Errors, Duration), USE method (Utilization, Saturation, Errors)
- **Logs** - you already did this well in Phase 4. Structured + correlated.
- **Traces** - OpenTelemetry basics, spans, distributed context
- **Alerting** - what's worth alerting on vs noise; SLO-based alerting
- **Dashboards** - build one you'd actually look at during an incident
- Load testing: `k6` or `locust`. Find your breaking point and report real numbers.

### Part F - Phase 6 projects

| Level | Project |
|---|---|
| Playful | Dockerize 3 of your old projects. Get each under 100MB. |
| Medium | Compose stack: FastAPI + Postgres + Redis + nginx, with migrations on boot |
| Medium | Full GitHub Actions CI for that stack, with a coverage gate that fails |
| Medium | Deploy to a managed host; custom domain; real TLS; automated rollback |
| Serious | Multi-stage, non-root, health-checked image + CI + registry + staging + prod |
| Serious | Load-test it, find the knee of the curve, tune, re-test, publish numbers |
| Serious | Add Prometheus metrics + Grafana dashboard + one meaningful alert |

**Phase 6 Exit Gate:**
- [ ] `git push` → live URL updated
- [ ] Image < 150MB, non-root, has a HEALTHCHECK
- [ ] CI blocks a bad PR (prove it by pushing a failing test)
- [ ] Rolling deploy with **no downtime** (verify by hitting it in a loop during deploy)
- [ ] Grafana dashboard + ≥1 alert that has actually fired
- [ ] You can explain every layer of your request path in prod using logs + metrics + traces

---

## Phase 7 - System Design

> You're a software engineer now. This phase is about building things that stay up when you're asleep.

### Part A - The vocabulary (memorize, then practice)

- **Latency numbers** - know the rough magnitudes: L1 ~0.5ns, RAM ~100ns, SSD ~100µs, same-DC network ~0.5ms, cross-continent ~150ms. Use them for estimation.
- **Throughput vs latency vs concurrency**
- **Availability & SLO/SLA/error budget** - 99.9% = 43 min/month of downtime. Compute it.
- **Load factors** - what drives your traffic? Users? Objects? Requests per user?
- **Little's Law** - `L = λW`. Use it in every estimation.
- **CAP theorem** - and PAC/PCAB in practice; you get consistency *or* availability during a partition, not "3 of 4"
- **Consistency models** - strong, eventual, read-your-writes, monotonic
- **Back-of-the-envelope math** - always start here. Storage, bandwidth, QPS.

### Part B - Data storage at scale

- **Relational vs document vs key-value vs wide-column vs time-series vs vector** - pick by access pattern, not hype
- **Indexing internals** - B-trees (read-heavy), LSM trees (write-heavy), inverted indexes (search), bloom filters
- **Normalization vs denormalization** - the join you do at write time instead of read time
- **Replication** - leader-follower, leaderless, read replicas, lag, staleness
- **Sharding** - hash (even, no range queries), range (flexible, hot spots), directory-based
- **Consistent hashing & the "hot shard" problem**; how shard keys are chosen
- **CAP in practice** - quorum reads/writes, `R + W > N`
- **Partition tolerance failures**: dual writes, split brain, rebalancing storms

### Part C - Scaling patterns

- **Vertical vs horizontal scaling**
- **Stateless services** - why statelessness makes horizontal scaling trivial
- **Load balancing** - round robin, least connections, consistent hash, least response time; health checks; sticky sessions and their cost
- **Caching** - the single highest-leverage tool
  - Layers: browser → CDN → reverse proxy → app → in-process → Redis → DB
  - Strategies: **cache-aside, read-through, write-through, write-behind**
  - Eviction: LRU, LFU, TTL, randomized
  - Stampede protection: request coalescing / locks
  - What to cache and what *never* to cache
- **CDN** - what it does, cache keys, purge, when to bypass
- **Rate limiting & throttling** - fixed window, sliding window log, sliding counter, **token bucket**, leaky bucket; where to enforce it; 429 + `Retry-After`
- **Async & messaging** - why you decouple, queue vs pub/sub, **Kafka partitions & ordering keys**, **exactly-once (and why you usually settle for at-least-once + idempotency)**, DLQs, backpressure, consumer groups, retries with backoff
- **Distributed transactions** - 2PC, saga pattern, outbox pattern, idempotency keys, eventual consistency in practice
- **Reliability patterns** - **timeout budgets**, **exponential backoff + jitter**, **circuit breaker**, **bulkhead**, **hedged requests**, **idempotency**
- **Observability at scale** - metrics cardinality, sampling, tracing cost
- **Multi-region** - active-active vs active-passive, geo-routing, data residency, failover

### Part D - Design patterns at scale (GoF you know + distributed variants)

Saga, CQRS, event sourcing, outbox, cache-aside, retry, bulkhead, circuit breaker, sharding, leader election, gossip protocol, anti-corruption layer, sidecar.

### Part E - The project ladder

#### Tier 1 - Playful implementations (build the primitive, not the service)
1. LRU cache from scratch → then with TTL
2. Token bucket rate limiter → then a distributed one on Redis
3. Thread pool / task executor from scratch
4. A minimal HTTP client with retries, backoff, and a circuit breaker
5. A mini message queue over `socket` (publish/subscribe, durability)
6. Consistent hasher with virtual nodes
7. A tiny reverse proxy with health checks and least-connections balancing
8. An inverted index + ranked search over 10k documents

#### Tier 2 - Medium systems
1. **URL shortener** - how you scale to 100M URLs (hashing, base62, sharding, cache, 301 vs 302)
2. **Notification system** - user preference service, template service, fanout to email/push/SMS, dedup, rate limit, DLQ
3. **File storage service** - presigned uploads, multipart, direct-to-object-storage, CDN
4. **Search engine** - index sharding, query fanout, ranking, freshness
5. **Event-driven order pipeline** - saga across services, idempotent consumers, DLQ replay
6. **Real-time chat** - connection management, presence, message ordering, fanout on write
7. **Rate-limited API gateway** - auth, quotas, routing, circuit breakers, observability
8. **Job scheduler** - cron parsing, leader election, distributed locking, retries

#### Tier 3 - Serious design exercises (write a full design doc, no code required)
- Design Twitter/feeds (fanout on read vs write, celebrity problem)
- Design a video upload + transcode + streaming pipeline (Netflix)
- Design Uber's dispatch (matching, geospatial, surge pricing, ETAs)
- Design YouTube's metadata + video serving (CDN, cold storage)
- Design a multi-tenant SaaS billing system (metering, isolation, quotas)
- Design a rate-limited payments system (exactly-once, idempotency, ledgers)
- Design a session store that scales to 100M users
- Design the database for a ride-hailing app's history (partitioning by time, hot partitions)
- Design a webhook delivery system (retries, signing, ordering, dedup)
- Design a feature-flag service (evaluation speed, stale reads, blast radius)

### Design doc template (use this for every exercise)

```
1. Requirements & constraints      (functional / non-functional, scale numbers)
2. Capacity estimates              (storage, bandwidth, QPS - show the math)
3. API / interface design
4. Data model & storage choices
5. High-level architecture         (diagram)
6. The hard parts, one at a time:
   - the write path
   - the read path
   - consistency & correctness
   - failure modes & recovery
7. Scaling & bottlenecks            (what breaks first? what breaks at 10×?)
8. Caching strategy
9. Reliability: retries, timeouts, idempotency, circuit breakers
10. Observability & SLOs
11. Security & abuse
12. Cost estimate
13. Alternatives considered & why rejected
14. What I'd build first (MVP path)
```

**Phase 7 Exit Gate:**
- [ ] Tier 1: 8 primitives built from scratch
- [ ] Tier 2: 4 systems designed + at least 2 partially implemented
- [ ] Tier 3: 10 design docs, each with a diagram
- [ ] Every design uses estimation math
- [ ] You can run a whiteboard system design interview for 45 minutes without stalling
- [ ] You've read (and can critique) at least one real postmortem

---

## Appendices

### A. Daily cadence

| Block | Time | Activity |
|---|---|---|
| 1 | 45 min | **Hard concept / problem solving.** The stuff you're bad at. Do this first. |
| 2 | 45 min | **Reading + notes.** Then immediately write code from memory. |
| 3 | 45 min | **Project work.** Ship something. |
| 4 | 15 min | **Write what confused you** in `NOTES.md`; commit. |

- **Weekly**: one review + one rest day. Rest is part of the plan.
- **Never** skip two days in a row. Momentum is the whole game.

### B. Progress tracker

Maintain a `PROGRESS.md`:

```markdown
## Phase 2 - OOP
| Item | Status | Notes |
|---|---|---|
| Polymorphism concept demo | done | quizlet-style review helped |
| Playlist manager | done | refactored to composition, better |
| Bank simulator | done | properties bug: setter validated wrong |
| Tic-tac-toe | in progress | state enum done |
| Blackjack | blocked | stuck on __hash__ - see BLOCKERS |
```

### C. The debugging playbook (living document)

```markdown
## Symptom: API returns 502 after deploy
- Date: 2026-03-14
- Environment: prod
- Root cause: container OOMKilled during startup; readiness probe never passed
- How found:
  1. `kubectl describe pod` → "Liveness probe failed: OOMKilled"
  2. `docker logs` → killed before any log line
  3. Confirmed with `dmesg | grep -i oom`
- Fix: raised memory limit 512Mi → 1Gi; fixed N+1 in startup query
- Prevention: added memory limit + OOM alert to Grafana
```

### D. Common pitfalls (check these before you spiral)

1. **Tutorial hell** - watching without typing. Stop.
2. **Learning frameworks before fundamentals** - you learned FastAPI before sockets. That's backwards; Phase 5 fixes it.
3. **Skipping math** - you *will* hit this ceiling in Phase 7.
4. **No version control from day one** - you lose the ability to see your own growth.
5. **Building no projects** - knowledge without artifacts is not skill.
6. **Ignoring error messages** - read the whole traceback, top to bottom, then bottom up.
7. **No tests** - you'll spend more time debugging than building.
8. **Deploying too late** - Phase 6 should not be your first time touching Docker.
9. **Learning too many things at once** - depth beats breadth, except in Phase 1.
10. **Not writing design docs** - thinking isn't designing. Write it down.

### E. Resources (pick one primary per topic; don't collect courses)

**Free & high-signal**
- *Python for Everybody* - Dr. Chuck (free, excellent)
- *Automate the Boring Stuff with Python* - free online
- *CS50x* (Harvard) - the missing CS degree, free
- *Missing Semester* (MIT) - **do this during Phase 3**, covers shells, git, editors, debugging
- *The Rust Programming Language* - only if you finish early
- *Computer Networking: A Top-Down Approach* - the free top-down version (Kurose & Ross)
- *Designing Data-Intensive Applications* - the system design bible (buy it)
- *System Design Primer* - free, GitHub
- *ByteByteGo / Hello Interview* - system design videos
- *The Pragmatic Programmer* - craft, mindset
- *Debugging* (David Agans) - the 9 rules; short, transforms you
- Official docs: `docs.python.org`, `docs.docker.com`, `kubernetes.io/docs`, `fastapi.tiangolo.com`

**Communities**
- r/learnpython, r/ExperiencedDevs, r/devops
- Python Discord, FastAPI Discord
- Ask questions *well*: minimal reproducible example, what you tried, what you expected

### F. Final note

The plan is 12 months of consistent work. Some people will do it in 8. Some in 18. The variable is not talent - it's whether you ship something every single week, and whether you can explain it to someone else.

**Build. Break. Read logs. Fix. Ship. Repeat.**

---

*Last updated: 2026-10-02*