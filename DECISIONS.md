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
| 3 | **Where the money goes** | **Split set 2026-09-24, internal only: 50% of revenue to the student stipend pool, 50% retained by the program.** The retained half is not broken out further. **Stipend is paid per client week (set 2026-09-24):** each client week with utilization credit pays the week rate, up to $312.50 (10 paid hours at $31.25; the first 10 of 20 weekly hours earn the course credit). Week rate = min($312.50, pool ÷ client weeks across all enrolled students), one rate for everyone since students set neither price nor staffing. The pool is cash collected by semester end; fall weeks are trued up once the rest of fall revenue is collected; a pool beyond the full rate carries to the next term. $312.50 is exactly what a $7,500 engagement (2 students × 6 weeks) funds, so underpriced or long engagements lower the rate. The 60% utilization threshold is a target only and no longer sets pay. Payment mechanics through BYU remain unresolved | Brian asked Allyson about payment timing and BYU vendor setup in July and it died when engineering declined. The mechanics are still the most urgent item |
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
| 12 | **Consultant axes** | Four, settled 2026-10-08: Judgment, Ownership, Communication, Collaboration. Derived from the Four Imperatives in STRAT 325: Judgment from Think Clearly and Get to the Right Answer, Ownership from Move Work Forward, Communication and Collaboration from Create Impact with People (understand and trust). Replaced Workstream Ownership, Client Hands, Communication, Collaboration, whose three people axes overlapped and which left Judgment out; the client relationship moved into Collaboration, and clients rate all four | Anchors written for all four, in `ops/developmentship-model.md` |
| 13 | **Consultant rating mechanics** | Proposed: faculty, teammates, and clients, midterm and end of term, 1 to 5 with written anchors | Syllabus says it feeds Client Evaluation and Peer / Team Evaluation without adding points. Untested |
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
| 20 | ~~Stipend~~ | **Reversed 2026-09-03. No stipend or compensation is promised anywhere.** All stipend language, the revenue waterfall, and the utilization model are removed from the syllabus, `06-builder-and-consultant.qmd`, and the welcome letter | The only money statement that remains is Claude plan coverage, below. Open item 3, where the money goes, is now internal only |
| 21 | ~~AI subscriptions~~ | **Reversed 2026-09-03. The Foundry covers a Claude plan**, either on the Foundry's Claude Enterprise account or by reimbursing a plan the student holds. No tier is named and no dollar figure is published; the plan and mechanism are set each term | Removes the cost-of-participation barrier. Confirm the Enterprise account can carry the seats before the term begins |
| 22 | ~~Constitution on the site~~ | **Resolved 2026-09-02. The published page is the binding version.** The Google Doc was an interim step to gather feedback and that feedback is now in. Amendments go through the faculty advisor, who updates the page | Members sign against this page in the welcome letter, so drift is now a contract question rather than a tidiness one |


## Added 2026-08-31: the three-track curriculum and the Developer certification

Scott's framing: the curriculum is three things. Actual client work, the Claude Developer
certification, and building your own project if you are not staffed. Two new pages implement it,
`students/08-certification.qmd` and `students/09-studio-projects.qmd`, both added to `_quarto.yml`
under "The Course".

### Why Developer, Foundations and not Architect

BYU is already a Claude Partner Network member. Three of Anthropic's four certifications count
toward network tier eligibility. Associate does not, and Anthropic states that on the
certification card itself.

Developer, Foundations is the efficient choice: $125, same tier value as Architect Foundations,
but four prep courses instead of seven. Anthropic's own role framing describes it as being for
"engineers who build with the Claude API, Claude Code, and Model Context Protocol", which is the
builder role exactly.

Target is **ten passes per year, every year**. Ten active certified individuals is one of the
three gates for Select tier, alongside two joint customers deployed in production in a trailing
twelve months and one public customer story. Certifications expire after 12 months, so the ten is
a standing annual target, not a one-time push.

### The staffing arithmetic that forced track three

Six concurrent engagements at capacity, two builder seats per pod, is twelve client seats against
thirty builders. Roughly sixty percent of the cohort is unstaffed at any time.

This means the guardrail in `students/05-how-teams-are-staffed.qmd`, "Nobody sits out a semester.
If you have zero engagements by the midpoint of the term, you get a directed placement into the
next opening", cannot be kept. There are not enough openings. Studio projects are the honest
answer, and that page now carries the arithmetic openly rather than promising placements that do
not exist. **The guardrail text in 05 still needs rewriting to match.**

### Open, and blocking a publish

| # | Item | Status | Why it matters |
|---|------|--------|----------------|
| 23 | **Syllabus does not reflect either new page** | Open | The 500-point table, the Milestone Deliverables section, and the Client Evaluation section all assume every student is on a client engagement. 224 of 500 points are unearnable by an unstaffed builder as currently written |
| 24 | **User evaluation replaces client evaluation for studio projects** | Proposed | Three real users answer the same five-dimension questionnaire the client answers. Untested, and the response rate is the obvious risk |
| 25 | **Exam is extra credit, prep is required** | Proposed | The four courses are free and inside our control, so they are required coursework. The sitting depends on Pearson scheduling and Anthropic pricing, so it does not gate a grade |
| 26 | **Who pays the $125** | Unresolved | Ten passes needs more than ten sittings. Budget roughly 15 at $125, about $1,875 in year one. The 50% partner discount only arrives at Select, which is the thing the sittings are meant to earn, so year one is full price. Ties to open item 3 |
| 27 | **Do student `@byu.edu` addresses clear exam registration?** | Untested | Registration requires "a partner email address on a recognized company domain". This is the single assumption the whole track rests on. Test with one student before scheduling a cohort |
| 28 | **Can an academic program be listed in the partner directory?** | Unknown | All 78 listed partners are commercial consultancies or systems integrators. No university appears anywhere in the directory |
| 29 | **Does a Foundry engagement count as a "joint customer deployed in production"?** | Unknown | The phrasing suggests a deployment made jointly with Anthropic. A student build for a paying client may not qualify |
| 30 | **Public customer story** | Open, and time-sensitive | One published story is a Select gate. Foundry policy is that nothing goes public without written client permission and that IP belongs to the client, so a public reference has to be negotiated at signing. Breckenridge is already underway, so that conversation happens separately and soon |

### Sourcing note

Exam specifications, the list of qualifying certifications, tier thresholds, policies, and prep
course lists are all confirmed on Anthropic's own pages. Several third-party prep sites publish a
five-domain blueprint with percentage weights for Architect Foundations that conflicts with
Anthropic's own description of that exam. Do not plan curriculum against those weights.

## Added 2026-10-22: two-week sprints and the sprint menu

- From 2026-10-23 every student runs two-week sprints (plan, output, review, Loom demo), staffed
  or not. The sprint replaces the individual weekly update email (forgiven through the week of
  Oct 12, with extra credit for those sent).
- Each sprint holds one or two items from the sprint menu: **Build** (any part of the value
  chain, for a client, the Foundry, or your own product; staffed students build for their client
  first) or **Learn** (a Claude course or Product Management book chapters, ending in proof).
- Fall grade: 3 sprints x 120 (Plan 10, Output 60, Review 25, Demo 25) + colleague and client
  feedback 140 = 500. Winter adds the client evaluation and the video reflection.
- Engagement length is set per client; the sprint calendar does not depend on it.
- The model is shared with MSB 341 and STRAT 477R; the spec is
  `byu-strategy/builder-template/.claude/sprint-model.md`.
- Still open: a Learn-only sprint once in fall when unstaffed; whether certification is expected
  of everyone; the extra credit amount; whether the client update stays; the staffing page
  rewrite (no points or auction since 2026-09-23).
