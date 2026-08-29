# Open Decisions

Everything in this repository reads as settled so the site works as a real program. Not all of
it is. Confirm before anything goes to a client or to CapSource.

Rewritten 2026-07-28 against the AI Foundry one-pager (`~/Desktop/AI-Foundry.pdf`), which
corrected several things the first draft had wrong.

## Confirmed by the one-pager

| Item | Value |
|------|-------|
| Positioning | An AI-native product studio and consultancy. "We ship, not advise" |
| What we deliver | Production software, integrated and running in the client's environment |
| Three offerings | Full-stack applications; AI integration and orchestration; AI enablement and training |
| Three phases | 01 Audit and discovery, 02 Build, 03 Transfer. Each buyable on its own |
| Engagement model | Fixed fee, scoped per phase (numbers set separately, see below) |
| Team | 30 builders, in mixed teams |
| Scott's title | Faculty Advisor, not Program Director |
| Status | An official program of the BYU Marriott School of Business |
| Domain and email | aifoundry.byu.edu, aifoundry@byu.edu |

## Confirmed elsewhere

| Item | Value | Source |
|------|-------|--------|
| Course numbers | MBA 693R-011, STRAT 490R-001 | AIM screenshot |
| Class time and room | Fridays 8:00–11:50 AM, 1244 TNRB | Fall 2026 teaching schedule |
| Credit hours | 3.0 per semester, per number | AIM screenshot |
| Intake | Rolling, no application deadline | Your call, 2026-07-28 |
| First client | Breckenridge Pharmaceutical, won 2026-07-28 | Email thread |

## What the one-pager corrected

The first draft of this site was built before I had seen it, from the BYU engineering capstone
RFPs. It was wrong in four material ways, all now fixed:

1. **It described the Foundry as delivering decision frameworks and models, not software.** The
   partner overview and FAQ listed "production software engineering" as an explicit **poor
   fit**. That is backwards.
2. **It priced the work at $22,000 per project for an academic year.** The real model is fixed
   fee scoped per phase, starting with a small discovery audit.
3. **It sized teams at 4 to 6 students** with no reference to the MBA bench.
4. **It called Scott "Program Director"** and invented `ai-foundry@byu.edu`.

## Still open

| # | Item | Status | Why it matters |
|---|------|--------|----------------|
| 1 | ~~Actual fee figures~~ | **Set 2026-08-01. See Pricing below** | Resolved |
| 2 | ~~How Breckenridge is priced~~ | **Resolved.** $22,000 for 8 months is exactly what they already expect from the engineering RFP. No exception, no reconciliation needed | Resolved |
| 3 | **Where the money goes** | Unresolved | Brian asked Allyson about payment timing and BYU vendor setup in July and it died when engineering declined. Still the most urgent item |
| 4 | ~~Capacity~~ | **Set 2026-08-12. Six concurrent engagements, seventh pod held as float.** See `ops/staffing-model.md` | Resolved |
| 5 | **Discovery-only vs full engagement grading** | Syllabus says discovery-only teams do D plus a scaled transfer | Reasonable but untested. If a client stops after discovery, that team ships no software and the milestone rubric leans on shipping |
| 6 | **Student hours** | Set at 10/week each, contractual not a range | Now load-bearing: it is the basis of the fee. Confirm 10 hrs supports 3.0 credits under BYU policy |
| 7 | **Office hours slot** | Fri 11:00 AM–12:00 PM | Placeholder inside the class block |
| 8 | **LMS** | Canvas | Product Management uses Canvas, APM Lab uses LearningSuite. Just confirm |
| 9 | ~~Site URL~~ | **Live at `byu-strategy.github.io/ai-foundry`** | Resolved |
| 10 | **Intake path** | Questions written (`client-facing/06-project-intake.qmd`), form not built | Needs to become a real Google Form on `aifoundry.byu@gmail.com`, linked from aifoundry.byu.edu |
| 11 | **Partner FAQ** | Deferred by Scott, 2026-08-12 | To be written for the official website, not here |
| 12 | **Program guide link from the website** | Not yet added | aifoundry.byu.edu becomes the default portal for everyone and routes students here for program details |
| 13 | **Are builders paid?** | Unresolved, see Pricing below | Decides whether $35/student-hour works at all |

## Pricing, set 2026-08-01

**Published:** $22,000 fixed fee for an 8-month engagement, covering all three phases. A
dedicated two-person build team at 10 hours each per week, plus a QC lead and faculty
oversight. 640 hours of delivery capacity.

**Internal derivation:** $35 per student-hour. 2 builders x 10 hrs/week x 32 weeks = 640 hours
= $22,400, rounded to $22,000. Do not publish the hourly figure; it invites "why does a student
cost that."

**Where $35 sits in the market:**

| Comparison | Rate per student-hour |
|---|---|
| Most CapSource business programs (Schulich, NYU Wagner, Stevens, Montclair) | $0 |
| BYU Engineering capstone | $8 to $17 |
| **AI Foundry** | **$35** |
| Notre Dame ESTEEM | $33 to $133 |
| Junior contract developer | $50 to $100 |
| Boutique consultancy, junior staff | $150 to $250 |

**Still unresolved and it matters:** whether builders are paid. If they work for credit only, as
APM Lab students do, $22,000 minus tooling and BYU overhead is program surplus and $35 is
comfortable. If you want to pay builders, even $20/hour consumes $12,800 of the $22,000 and the
rate stops working. Decide this before the second engagement.

**Also unknown:** what BYU takes off the top. If there is an indirect cost recovery on sponsored
activity, the effective rate is lower than $35 and possibly much lower.

**Revisit after Breckenridge ships.** $35 is deliberately low for a first cycle. Reference
clients and case studies are the scarce thing right now, not margin.

## Tension worth deciding deliberately

**CapSource's format is an academic capstone RFP. The one-pager is a consultancy.**

Every engineering page Jordan runs has the same shape: fixed annual sponsorship fee, student
teams, a semester calendar, a design fair. The Foundry sells phased fixed-fee engagements with
rolling intake and ships production software. Those are different commercial products.

The RFP in this repo leads with the consultancy and keeps only the pieces a sourcing page needs.
That is the right call, but it means Jordan's page will not look like the engineering pages, and
companies arriving from the engineering funnel will have different expectations. Worth saying
to him explicitly rather than letting him discover it.

## Deliberate choices worth reviewing

- **Peer evaluation carries individual differentiation, client evaluation is team-level.**
  Protects against a client who likes the outgoing student and undervalues the quiet one, but it
  means students grade each other.
- **The syllabus has a hard confidentiality section with an Honor Code hook.** Real client data
  and student portfolios collide constantly.
- **"What We Do Not Do" is on the partner overview.** Filters bad-fit inbound before it costs a
  call, which matters more once CapSource is generating volume.

## Added 2026-08-12: the two-shape framework

Introduced on the site in `index.qmd`, `students/01-syllabus.qmd`, and
`students/02-getting-started.qmd`. Grew out of the August baseline survey of 12 students.

| # | Item | Status | Why it matters |
|---|------|--------|----------------|
| 11 | **Builder axes** | Six, settled: Discovery, Design, Application Architecture, AI Systems, Agentic Workflow, Launch and Learn | 50-item self-report instrument is live and has one cohort of responses |
| 12 | **Consultant axes** | Four, settled: Workstream Ownership, Client Presence, Communication, Collaboration. Derived from the Four Imperatives in STRAT 325 | Behavioral anchors drafted for Workstream Ownership only. The other three are not written yet |
| 13 | **Consultant rating mechanics** | Proposed: faculty plus teammates, midterm and end of term, 1 to 5 with written anchors | Syllabus says it feeds Client Evaluation and Peer / Team Evaluation without adding points. Untested |
| 14 | **Tiers: Shadow, Contribute, Own** | Proposed | Replaces the earlier idea of a hard prerequisite. Not yet reflected in the milestone rubric, which assumes everyone ships |
| 15 | **Prerequisite removed** | Settled. `index.qmd` no longer says students typically complete MSB 341 first | Two classes run in parallel. Readiness affects staffing, not enrollment |
| 16 | **Baseline survey cadence** | Proposed: September and December | December re-run has not happened. Comparison claim is untested |


## Added 2026-08-12: staffing model, intake, and the site split

Three things settled in one sitting, prompted by the Indigo Institute inbound.

### The site is student-facing only

The Lab site was serving students, sponsoring partners, and prospective sponsors at once. It now
serves students only. `partners/` moved to `client-facing/` and is out of the render. The
official website, `aifoundry.byu.edu`, is the default portal for everyone and will link here for
program details.

`client-facing/` is porting source, not a maintained second copy. Delete it once the content is
on the website. Two copies of the commercial terms is exactly how they drift.

### Staffing model

Full rules in `ops/staffing-model.md`, student-facing version at
`students/05-how-teams-are-staffed.qmd`.

- **The pod** is the unit: engagement lead (MBA, up to 2 engagements), two builders (10 hrs/week,
  one engagement each, never shared), QC lead (up to 4 pods), design lead on demand, faculty
  oversight. Matches what the published terms already promise.
- **Six archetypes** classify projects and rate builders 0 to 3. A pod needs a 3 in the primary
  archetype plus a second 3 on the bench as backup. Failing that, no build phase.
- **Capacity is 6 concurrent engagements**, seventh pod held as float. Closes open item 4.
- **One pod ships one product surface.** More than one product is more than one engagement, at
  its own fee. Now stated on the site and in the intake questions.
- **Three risk tiers.** Anything where an AI output influences a decision about a person is
  Restricted, staffed by appointment, and carries a written carve-out: the client owns the
  decision and its validation.

### The points market

100 points per month per builder, capped at 300, reset to zero on winning a seat. Fit gates
eligibility first, Builder A is appointed against the matching rule, Builder B is auctioned to
eligible bidders by sealed **second-price** bid.

Second-price is deliberate: it makes bidding your true interest the dominant strategy, which is
the only reason the mechanism is worth its complexity. Pay-your-bid in a market this thin would
just reward whoever guesses the field best.

**Open:** the auction has never run. Watch for two failure modes in the first cycle. One,
everyone bids 300 on the same glamorous project and the clearing price says nothing. Two, an
unglamorous but well-fitting project attracts one bid and clears at 1, which is fine but looks
like nobody wanted it. Neither is fatal. Both are worth seeing before the rules harden.

**Also open:** whether the 300 cap is right. It was picked, not derived.

### Intake

Questions at `client-facing/06-project-intake.qmd`, internal screening rubric and worked example
at `ops/client-intake-form.md`. Every question maps to a staffing, scoping, or pricing decision.
The rubric scores fit 0 to 12 with two automatic declines: no bench coverage, and no committed
sponsor.

Not yet built as a form. That is open item 10.

### Indigo Institute, the case that prompted this

Two projects in one email: an AI video interviewing and candidate screening tool, and a
next-generation LMS. Run through the rubric this is **two engagements at $22,000 each**, not one.
The screening tool is Restricted tier because it scores candidates for admission to a program
that feeds job placement. The LMS as described is well over 640 hours and should be sold as
discovery first, cut to one shippable surface. Kim Moore is an attorney, so the adverse-impact
conversation will be easy to have and expensive to skip.

## Added 2026-08-12: prerequisite, pathways, and the stipend

| # | Item | Status | Why it matters |
|---|------|--------|----------------|
| 17 | **Prerequisite** | Steady state: Build, IS 693R / MSB 341, is required, offered fall and winter. Exceptions granted for 2026-2027 only | Site now states it as policy with a footnote. Confirm the catalog can carry it, or that instructor consent is the mechanism |
| 18 | **Three pathways for 2026-2027** | Published from Scott's 2026-08-12 email to the cohort | Option 2 asks students to carry both classes at once. No one has done that yet |
| 19 | **Student hours** | Published as 10 hours per week | Same as open item 6. Now student-facing, so it is harder to walk back |
| 20 | **Stipend** | Published as: applied to the student account, follows a funded engagement, not employment, intended to also cover AI subscription costs. No amounts published | Mechanism, timing, and who administers it are unresolved. Ties to open item 3, where the money goes |
| 21 | **AI subscriptions** | Students carry their own. The Foundry does not provide seats | Sets a real cost of participation. Confirm this is what you want before students enroll |
| 22 | **Constitution on the site** | Full text published at `students/00-constitution.qmd` | Living version stays the team Google Doc. The site copy will drift unless someone re-syncs it |

