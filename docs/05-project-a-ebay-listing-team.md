# Project A - eBay Listing Team

Five vintage guitar pedals, five listings, one unhurried afternoon.

## The project brief (fictional but realistic)

You clear out a small batch of guitar pedals from a storage-unit sale — five pedals, no manuals, three with visible serials. You want solid, honest eBay listings this weekend, and you refuse to write them at midnight on your phone. This is the classic single-agent trap: one conversation researches five products and writes five sales listings, and by pedal four it is confidently confusing the pedals with each other.

A team fixes this by shape, not by effort: the researcher never writes prose, the writer never invents specs, and the checker compares every listing claim against its fact sheet before you hit publish.

> Education note: this project is a learning exercise. Follow your marketplace's current policies before listing anything real, and get price expectations from sold listings, not vibes.

## The roster

| Role | Filled by | Owns | Produces |
| :--- | :--- | :--- | :--- |
| Boss | You | kickoff.md, moves to final/ | approvals |
| Planner | Planner chat | kickoff.md (drafts it) | kickoff + task memos |
| Researcher | Researcher chat | facts/ | 5 fact sheets |
| Writer | Writer chat | drafts/ | 5 listing drafts |
| Checker | Checker chat | notes/ | review memos |

Four agents (plus you, the boss), four short conversations. Every "chat" is just a fresh conversation with its role description pasted at the top. Total setup, under fifteen minutes.

## The folder

```
pedals-project/
  kickoff.md
  log.md
  notes/
  facts/
  drafts/
  final/
  archive/
```

Create it yourself in two minutes, or have your planner agent list it (never have an agent create folders *unannounced* on anything you care about — you are the boss of the floor plan).

## Step 1 — Write the kickoff (you + planner, one short chat)

Paste this to your planner chat:

```
You are my Planner. Write my kickoff.md (draft only) for this project.
Goal: create 5 honest eBay listings for 5 vintage guitar pedals.
Definition of done: one listing per pedal in final/, every claim traceable
to its fact sheet, unknown values marked "not stated", I approve each one.
Roster: me (BOSS, approvals), RESEARCHER (facts/), WRITER (drafts/),
CHECKER (notes/ memos only). House rule: one writer per file; questions
go in notes/questions.md. Folder is pedals-project/. Keep it under 25 lines.
```

A good planner drafts the five-line kickoff from the roles chapter. Read it, fix it, save it as `kickoff.md`. (This sample draft is used by all the later steps.)

## Step 2 — Staff each chat (paste the role card)

To the researcher chat:

```
You are my RESEARCHER. You own facts/ (one file per pedal).
You produce fact sheets only — no marketing language, no guesses.
Format: item, model, serial (if visible), condition notes, best
sold-listing match for model/type, typical price range from recent SOLD
listings, sources (links), open items. When unsure: stop and write the question
to notes/questions.md. Log one line to log.md when done.
```

To the writer chat, the same pattern; to the checker chat add: `You NEVER rewrite drafts. You write review memos in notes/.` Copy those role cards — they are most of the value of this page.

## Step 3 — The research pass (researcher)

Hand the researcher the kickoff and your item notes. Abbreviated sample output — `facts/pedal-02-facts.md`:

```
STATUS: DRAFT (researcher)
# Pedal 02 — "Phase Shifter" (three knobs, teal paint, scuffed)
- Model: best guess "Phase Shifter" pedal, similar to 1970s 'phase' pedals; EXACT model NOT confirmed
- Serial/plate: none found; no date codes visible
- Condition: teal paint scuffed on corners; knobs original; no adapter included
- Sold-comp price range: $40–120 depending on brand/model (sources: 6 recent sold listings)
- Sources: [seller photos analyzed: ITEM-02-photo1..4] [sold listings: 6 links]
- Open items: brand unknown (logos worn); exact model unknown
- Watch out: do NOT list decade or brand as fact. Listing must say "unbranded".
2026-03-01 RESEARCHER logged: pedal-02 done with 2 open items
```

That final "Watch out" line is exactly what makes the whole system run.

## Step 4 — The writer pass, with the handoff (researcher → writer)

The researcher's handoff memo (`notes/handoff-writer-1.md`):

```
HANDOFF — RESEARCHER to WRITER
DONE: all 5 fact sheets in facts/. 3 pedals fully identified (01, 03, 05).
2 have open items (02 brand unknown, 04 power-adapter voltage unstated).
NEXT: draft one eBay listing per pedal in drafts/, using ONLY fact-sheet
fields. Title ≤80 chars, 120–180 word description, condition honest,
shipping/me terms from kickoff.md. Unknown = "not stated", never guessed.
WATCH OUT: pedal-02 must be listed "unbranded" and "model unstated";
pedal-04 voltage: "verify with seller" if it stays unknown.
```

Sample writer output (`drafts/pedal-02-listing-DRAFT.md`, abbreviated):

```
STATUS: DRAFT (writer)
TITLE: Vintage Teal Phase Shifter Guitar Pedal - Unbranded - Untested - Ships Free
DESCRIPTION (draft): Vintage unbranded phase shifter pedal, teal finish with
honest wear. Untested (no adapter) — sold as-is, exactly as photographed.
Knobs appear original. Classic phase-pedal look perfect for boards or repair
projects. Ships free from a smoke-free home. Ask any questions before buying.
CLAIM MAP: unbranded->fact02 [researcher] | untested->fact02 [no adapter]
| knobs original->fact02 | teal paint->fact02 | smoke-free->my terms
```

The **claim map** is a habit worth stealing: every claim in the draft mapped to the fact file it came from. Making a claim-map is a one-line instruction to the writer ("append a CLAIM MAP listing each factual sentence and its source field") — it gives the checker (and you) a complete to-do list.

## Step 5 — The checking pass (checker)

Paste the role card plus the draft and its fact sheet side by side. Sample checker memo (`notes/review-pedal-02.md`):

```
REVIEW MEMO — pedal-02, round 1 (CHECKER)
STATUS: BOUNCE (needs 1 fix, 1 OK)
1. "Knobs appear original" — fact sheet says knobs original. Stated as
   appearance, matches evidence. OK.
2. CLAIM MAP lists "smoke-free" as source "my terms" — kickoff.md has no
   shipping/terms section yet. TODO: drop the claim, or add terms to
   kickoff.md with the boss's approval, then keep the claim.
APPROVE AFTER: item 2 resolved. Resend claim map for spot-check.
```

The writer fixes, logs one line, and resends. The checker's next memo reads, in part:

```
REVIEW MEMO — pedal-02, round 2 (CHECKER)
STATUS: APPROVED (smoke-free claim removed; claim map clean).
Next: boss moves draft to final/ at their own pace.
Logged: pedal-02 approved, round 2.
```

## Step 6 — You approve, the team ships

Read each final draft yourself — two minutes per listing, worth it. Flip each to `STATUS: APPROVED`, move files into `final/`, and list at your pace. Rename nothing; log one line per publish. The folder becomes a record: what was listed, what evidence it was based on, what the checker said.

## Adapt around and reuse

- **Extra honesty boosts sales** in reselling: "unbranded, model unstated" reads as *honest* to experienced buyers, not sloppy. The team form makes this natural — that is its point.
- **Do a 2-pedal pilot first** if you are new to teams. Five is a fine repeat number: the folder and role cards are already written.
- **Same shape, other projects:** a cleaning-out-the-garage team, a Flipping-finds team, a book lots team — anything where honest description plus price research beat intuition.

## What this project taught (in case you skimmed)

- Roles keep skills separate: research vs. writing vs. checking.
- Handoff memos carry context without history.
- The CLAIM MAP is a lightweight acceptance test the checker can actually verify.
- One bounce from a fresh-eyes checker is the whole return on investment: an unsupported claim never reached a live listing.
