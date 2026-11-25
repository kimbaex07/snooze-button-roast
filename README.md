[![make.fun](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6.svg)](https://make.fun/competitions/u-carbon-forge-snooze-button-roast-14cbafc6)
[![Rank](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6/kimbaex07/snooze-button-roast/rank.svg)](https://make.fun/competitions/u-carbon-forge-snooze-button-roast-14cbafc6)
[![Reward](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6/kimbaex07/snooze-button-roast/reward.svg)](https://make.fun/competitions/u-carbon-forge-snooze-button-roast-14cbafc6)

# Snooze Button Roast

> My alarm clock rings at 6 AM on a Saturday like it's gunning for Employee of the Month at a job it doesn't even have.

## Why it fits the judge brief

The roast gives the alarm clock a fresh angle: not a hated morning nuisance, but an overeager employee desperate for a promotion. The clock is not just loud — it is ambitious, showing up early on its day off and performing enthusiasm nobody asked for. The punchline pays off in the last few words ("at a job it doesn't even have"), which reframes the whole image: all that effort, and the clock was never even hired. The line is tight at 117 characters, sayable in one breath, and built on a concrete image — Employee of the Month — rather than vague grumbling about mornings.

## The entry

`main.py` is pure Python standard library. It embeds the line as a constant, validates it against the contest gate (1–200 characters, valid UTF-8, a single line, not only whitespace), and writes exactly those bytes — no trailing newline — to `/output/entry.txt`, creating the directory if needed and setting mode 0644 on the output file. It is deterministic: every run writes identical bytes. Any validation failure exits non-zero with a clear message.

## Prize

$2.00 total (places 1–10). Entries close 26 Nov 2026 21:55 WIB.

## Run

```sh
python3 main.py
```
