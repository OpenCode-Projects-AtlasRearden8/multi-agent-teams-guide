# Project C - Household Paperwork Team

Fifteen minutes a week, one folder, and no more "where IS that bill?" moments.

## The project brief (fictional but realistic)

A household that runs on a shoebox: envelopes from insurance, delivery receipts, a school form, two pharmacy printouts, a parking notice, and (every March) a tax-season panic. You want a weekly fifteen-minute ritual where a small team of agents turns the week's paper pile into one tidy summary and one prioritized to-do list — low energy, ADHD-friendly, nothing clever required on a bad day.

Why a team beats one agent here: the work splits naturally into **sorting** (what even is this document?), **extracting** (dates, amounts, deadlines), and **summarizing into one page**. One long agent conversation over forty documents turns into mush — every item starts sounding like every other item. Three narrow agents each keep it short.

> Education note: this project handles *practice* documents only — fictional stand-ins. Never upload real personal documents (or anyone's real IDs, medical, insurance, or tax papers) into a cloud AI you haven't cleared. The safe-for-home pattern below works entirely with made-up examples; real documents go in the real drawer, and agents never touch them. This guide is education only, not legal, tax, or medical advice.

## The roster

| Role | Owns | Produces |
| :--- | :--- | :--- |
| Boss (you) | kickoff.md, final/ | approvals, transcribes paper into practice docs |
| Sorter | facts/ (one card per document) | sort cards |
| Squeezer | facts/ | deadline-and-amount summaries |
| Summarizer | drafts/ | the weekly one-pager |
| Checker | notes/ | catch-it memo (dates, math, double-counted items) |

"Squeezer" is our nickname for the extractor: it squeezes the juice (dates, amounts, deadlines) out of each sort card into one totals table. Rename the roles anything you like — but keep them narrow.

## The folder

```
paperwork-team/
  kickoff.md          <- includes "sensitive items" rule (below)
  log.md
  notes/
  inbox-practice/      <- this week's fictional practice documents
  facts/              <- one sort card per document (fictional examples only)
  drafts/
  final/
  archive/
```

Same rooms as every project. Reusing the same floor plan across projects is itself a feature: you stop re-deciding logistics, which is exactly where low-energy days go to die.

## The sensitive-items rule (write this into the kickoff before anything else)

- **Practice documents only.** Anything typed into this folder gets fictional names, fictional account numbers (`#####-99` style), and fake dates from this year.
- **Real documents stay real-world:** originals in a physical drawer or a scanned folder the agents never see. Agents get the *shape* of your paperwork, never its contents.
- **Never in play:** passwords, medical details, government IDs, real addresses or phone numbers, bank one-time codes. If a document is that sensitive, it simply does not exist from the agents' point of view.

This is the heart of the project: you get the *method* without ever exposing the *material*.

## Step 1 — Kickoff (you + planner, one short chat)

```
Goal: weekly 15-min paperwork ritual: inbox pile -> one summary page + one
prioritized to-do list.
Definition of done: weekly-summary-YYYY-MM-DD.md in final/, every deadline
and amount traceable to a sort card in facts/, checker memo attached.
Roster: BOSS; SORTER (facts/); SQUEEZER (facts/ totals table);
SUMMARIZER (drafts/); CHECKER (notes/). One writer per file.
Sensitive rules: practice documents only; fictional names/numbers/dates.
Energy rule: on low-energy days, BOSS may run sorter-only and skip steps.
Time-box: 3 passes max per week.
```

That last line — the **energy rule** — is what makes this project ADHD-friendly in practice. Teams don't have to run full-length every week.

## Step 2 — Sort pass (sorter)

You drop this week's practice documents into `inbox-practice/` (three fictional stand-ins: a fake utility statement, a fake tuition-form reminder, a fake delivery receipt). The sorter produces one card per document, format:

```
STATUS: DRAFT (sorter)
CARD: utility-statement-2026-03
TYPE: utility bill (electricity)
WHO: practice utility company
DATE ON DOC: 2026-03-01   DUE: 2026-03-18 (stated)
AMOUNT DUE: $84.12 (stated)   AUTOPAY: NOT STATED
ACTION NEEDED: pay by due date (or confirm autopay in real-drawer copy)
WATCH OUT: amount differs from last month's $71.03 — ask household why
```

That WATCH OUT is the quiet hero of the whole project: the *question* gets captured the moment it is noticed, instead of at 11 p.m. when you finally match numbers.

## Step 3 — Squeeze pass (squeezer)

The squeezer condenses all cards into one totals table, `facts/totals-2026-03-01.md` (abbreviated):

```
STATUS: DRAFT (squeezer)
| Item | Due | Amount | Needed? |
| utility-03     | 2026-03-18 | $84.12 | pay or confirm autopay |
| tuition-form   | 2026-03-15 | n/a    | signature + drop-off |
| delivery-receipt | none     | $0     | file only |
TOTAL DUE THIS WEEK: $84.12 | NEXT DUE DATES: 03-15 then 03-18
Watch-out count: 2 (utility amount change; tuition form needs signature)
```

## Step 4 — Summarize (summarizer)

`drafts/weekly-summary-2026-03-01-DRAFT.md` (abbreviated):

```
STATUS: DRAFT (summarizer)
# Weekly One-Pager — week of Mar 1 (practice documents)
MONEY DUE: $84.12 between now and Mar 18.
DO FIRST (5 min): sign tuition form by Mar 15. Envelope ready on the fridge.
MONEY QUESTION: electric bill went $71.03 -> $84.12. Ask: rate change?
 furnace? washer? (2-min curiosity, no dread.)
FILE: delivery receipt — archive/ if anything goes wrong later.
NEXT WEEK'S HINT: one non-agent item sits in the real drawer (agents: skip).
CLAIM MAP: every dollar and date above -> facts/totals-2026-03-01.md
```

The one-pager is deliberately short: three lines of action, one line of admin, one question marked for human attention. It fits on a phone screen on a tired Tuesday.

## Step 5 — Check (checker)

Sample checker memo (`notes/review-week-2026-03-01.md`, abbreviated):

```
STATUS: APPROVED (0 fixes, 1 compliment)
- Totals say $84.12; card amounts are $84.12 + $0 + n/a — consistent, good.
- Tuition form marked "n/a" — no invented money, good.
- Good catch by design: the summary mentions the real-drawer item only
  anonymously ("one non-agent item sits in the real drawer") — no document
  type, no name. Exactly the right level of detail.
PASS otherwise: totals match, dates match cards, one question flagged only.
```

The tone to preserve: the checker changes **nothing**. The summarizer applies fixes and logs; you approve; the file moves to final/. Your Sunday fifteen minutes: read the one-pager, answer the money question if you feel like it, mark done.

## Step 6 — The weekly ritual in real life

- **Same day, same place** (Sunday with coffee worked for our fictional household): it is a fifteen-minute meeting you hold with your tiny staff.
- **Worst weeks:** run sorter-only (one step, five minutes). A half-built summary beats a guilt spiral every single time.
- **March and other scary months:** the totals tables in `facts/` become your prep binder — the folder is tax-season ready without a single re-scan.

## What this project taught

- Some projects are about **volume, not quality** — a narrow pipeline beats one brilliant agent.
- The **energy rule** (optional steps, never mandatory guilt) is what makes a routine survive contact with real life.
- Sensitive data handling is a *kickoff rule*, not software: agents get practice documents, forever.

## Three real-shaped wins from our test run

- The $84-vs-$71 utility jump got captured as a *curiosity question* instead of a 2 a.m. spreadsheet mystery.
- The tuition form earned the one-pager's "DO FIRST" slot plus an envelope reminder, and was signed three days early (practice calendar).
- Zero real personal details ever entered an agent conversation, and the checker even caught a *shape-level* hint leaking into a summary — exactly the muscle you want trained on a team that might someday handle real work.
