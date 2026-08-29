# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Quarto book for the **BYU AI Foundry**, a year-long sponsored-project studio in the BYU
Marriott School of Business. Cross-listed as **MBA 693R** (section 011, Special Topics in
Management) and **STRAT 490R** (section 001, Topics in Strategic Management), Fridays
8:00 to 11:50 AM in 1244 TNRB, 3.0 credits per semester.

**This site is student-facing only** as of 2026-08-12. It is the program guide for people
enrolled in the Lab. Client-facing content moved to the official website, `aifoundry.byu.edu`
(repo `ai-foundry-byu/website`), which is the default portal and will link here for program
details. Do not add partner or sales content to this site.

Mirrors the structure of `byu-strategy/apm-lab`, with cross-listing presentation borrowed from
`byu-strategy/product-management`.

## Build Commands

- **Preview during development**: `quarto preview`
- **Check installation**: `quarto --version`

**Never render locally.** The site auto-renders via GitHub Actions on push to main. See
`.github/workflows/publish.yml`. Output goes to `docs/`.

## Content Structure

```
index.qmd                       # Program guide front page, cross-listing, commercial shape

students/                       # everything rendered
  01-syllabus.qmd               # Grading, policies, confidentiality, AI use, BYU boilerplate
  02-getting-started.qmd        # Onboarding, team roles, first two weeks
  05-how-teams-are-staffed.qmd  # Pods, archetypes, matching rule, the points auction
  03-weekly-updates.qmd         # Weekly client email format and examples
  04-build-standards.qmd        # Quality bar, repo standards, decision log, QC gate

client-facing/                  # NOT rendered. Porting source for aifoundry.byu.edu
  01-program-overview.qmd       # Structure, milestones, what we do and do not do
  02-working-with-the-team.qmd  # Cadence, scoping, scope changes
  03-evaluation.qmd             # Mid-year and end-of-year feedback
  04-faq.qmd                    # Cost, IP, confidentiality, fit, hiring
  05-rfp.qmd                    # Partner-sourcing page
  06-project-intake.qmd         # Client intake questionnaire, never published

ops/                            # NOT rendered. Internal, never published
  staffing-model.md             # Pods, capacity, risk tiers, the points market rules
  client-intake-form.md         # Intake questions, screening rubric, worked example
```

## Cross-Listing Pattern

Two places carry the course numbers, following `byu-strategy/product-management`:

1. `_header.html` injects `.sidebar-course-numbers` under the sidebar title
2. `index.qmd` and `students/01-syllabus.qmd` open with a `.course-numbers-page` div, followed
   by a "Course Numbers" section with the section-and-title table

Styles for both classes live at the bottom of `styles.css`.

## Program Context

- **Positioning**: an AI-native product studio and consultancy. We ship production software, we
  do not deliver reports. Source of truth is the one-pager, `~/Desktop/AI-Foundry.pdf`
- **Three offerings**: full-stack applications; AI integration and orchestration; AI enablement
  and training
- **Three phases**: 01 Audit and discovery, 02 Build, 03 Transfer
- **Pricing (set 2026-08-01)**: $22,000 fixed fee for an 8-month engagement. Derived from $35
  per student-hour: 2 builders x 10 hrs/week x 32 weeks = 640 hours = $22,400, rounded to
  $22,000. Publish the $22,000 and the team shape; the hourly is internal. Discovery-only is
  scoped separately and priced smaller
- **Team**: 30 builders in mixed teams, MBAs plus undergraduate builders. Per-engagement roles
  are client lead, builders, QC lead
- **Intake**: rolling. No application deadline, no fixed milestone calendar. Phase dates are set
  per engagement at kick-off. Do not reintroduce fixed dates into partner-facing pages
- **Scott's title**: Faculty Advisor
- **Contact**: aifoundry.byu.edu, aifoundry@byu.edu
- **Key student deliverable**: weekly client update, sent Saturday by 11:59 PM by the client lead

## Open Decisions

See `DECISIONS.md`. Several program parameters are proposed defaults, not confirmed policy.
Do not present them to clients as final until that file is cleared.

## House Style

- No em dashes anywhere in this repository
- Plain, factual prose. Scott adds the flourishes
