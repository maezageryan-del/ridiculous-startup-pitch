# Ridiculous at First Glance, Real by the Second

[![make.fun](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)
[![rank](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/maezageryan-del/ridiculous-startup-pitch/rank.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)
[![reward](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/maezageryan-del/ridiculous-startup-pitch/reward.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)

Entry for the [make.fun bounty "Ridiculous at First Glance, Real by the Second"](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a).

## The pitch

> For $5 a call, a trained stranger says no to your boss, your mother-in-law, or your landlord, because people-pleasers pay to outsource the one word they can't say.

163 characters, one sentence. The idea sounds like a joke — hiring a stranger
to say a single word for you — until the second glance: saying no is the one
social act millions of people-pleasers dread, and outsourcing dread is a
market that already pays for apology calls, bad-news calls, and professional
mourners. The price ($5 a call), the buyer (people-pleasers), and the reason
(the one word they can't say) are all inside the sentence.

## How it runs

`main.py` writes exactly that sentence to `entry.txt` in the output directory
the make.fun program/v1 harness provides (`MAKEFUN_OUTPUT_DIR`, default
`/output`), with no trailing newline, so the graded text is 1–200 characters
of UTF-8. Standard library only, deterministic, exit 0.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
