# ai-foundry

Student program guide for the **BYU AI Foundry**.

Cross-listed as **MBA 693R** (011) and **STRAT 490R** (001). Fridays 8:00 to 11:50 AM,
1244 TNRB. 3.0 credits per semester, 6.0 across the year.

Quarto book. Auto-renders to `docs/` and deploys to GitHub Pages on push to main.

## Audience

**Students only**, as of 2026-08-12. This site is the program guide for people enrolled in the
Lab: syllabus, onboarding, how client teams are staffed, weekly updates, and build standards.

Everything client-facing now lives on the official website, `aifoundry.byu.edu`
(repo `ai-foundry-byu/website`), which is the default portal for everyone. The program guide
will be linked from it. The former partner pages are parked in `client-facing/` as porting
source and should be deleted once ported, not maintained in parallel.

Internal operating documents that are not published anywhere are in `ops/`.

## Local development

```bash
quarto preview
```

Do not render locally. CI renders on push.

## Status

Content is complete and internally consistent, but several program parameters are proposed
defaults rather than confirmed policy. See `DECISIONS.md` before publishing or sending anything
to a client.

## Lineage

Structure mirrors `byu-strategy/apm-lab`. Cross-listing presentation follows
`byu-strategy/product-management`.
