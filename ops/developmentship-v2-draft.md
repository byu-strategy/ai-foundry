# The Developmentship Model, v2

*Working draft, 2026-10-08. For iteration with Scott. Nothing here is published or built.
The current model is [developmentship-model.md](developmentship-model.md) (internal) and
[students/10-developmentship.qmd](../students/10-developmentship.qmd) (public course site).
Both stay as they are until this draft is settled.*

Developmentship is how members of the AI Foundry develop one another through shared work, and
how an individual grade is determined. A grade is a synthesis of evidence from several sources,
each read against two published frameworks: the Builder hexagon (what you can make) and the
Consultant diamond (how you work when the work belongs to someone else).

## What changes from the current model

| | Current model (v1) | This draft (v2) |
|---|---|---|
| Frameworks measured | Consultant diamond only. The hexagon is excluded on purpose ("Why not the Builder hexagon") | Both the hexagon and the diamond |
| Sources | Three: peers, clients, self (plus optional faculty on the peer form) | Four: colleagues, clients, self, testing center. A fifth, an observed build, is planned |
| Faculty | Rates on the peer form, optional | Unchanged. Faculty fills in the colleague form; there is no separate faculty form |
| Constitution | Positive-only principle citation, never rated | Unchanged |
| Live feedback | Fifteen minutes every two weeks, not collected | Kept, with a guide (Appendix H) and a rule for when to talk and when to use the form (section 5) |

Kept from v1 without change: the exposure list, the self-assessment closing before anything is
released, the anchors, the three-rater floor, the two releases a semester, evidence required for
a 1, 2 or 5, and comments reaching the student only as unattributed themes.

## 1. The two frameworks

**The Builder hexagon.** Six axes: Discovery, Design, Application Architecture, AI Systems,
Agentic Workflow, Launch and Learn. Fifty skills underneath them, each rated on a five-point
scale from "New to me" to "Teach it." Full list in Appendix A.

**The Consultant diamond.** Four axes: Judgment, Ownership, Communication, Collaboration. Two
about the work (is it the right work, does it move), two about people (do they understand it, do
they trust you). Each rated 1 to 5 against written anchors. Full anchors in Appendix B.

**The constitution** is the standard behind both. It has fourteen principles under four
commitments (Appendix C). Nobody is rated on a principle. Every form asks one optional,
positive-only question: which principle did you see this person live, and what did they do?

Judgment runs through every Builder axis, Discovery most of all. That overlap is deliberate: the
hexagon reads judgment as it shows up in an artifact, and the diamond reads it as it shows up in
decisions other people watched someone make.

## 2. Four sources of insight

| # | Source | Who | Instrument | When |
|---|---|---|---|---|
| 1 | **Colleagues** | Every Foundry member on the student's exposure list, and faculty | Colleague feedback form (Appendix D) | When the shared work ends |
| 2 | **Clients** | Every client contact on the engagement | Client team review (Appendix E) | End of every 5-week block |
| 3 | **Self** | The student | Builder self-assessment (Appendix A) and Consultant self-assessment (Appendix F) | Builder: September and December. Consultant: closes before each release |
| 4 | **Testing center** | The student, proctored, no AI | Exams (Appendix G) | Midterm and final |
| 5 | *Later:* **Observed build** | The student, watched or recorded | A hands-on build task, or an assessment of how they work with AI. Not designed yet | Not set |

Sources 1 and 2 report what someone **observed**. Source 3 asks the student to **predict and
produce evidence**. Source 4 **tests** what a student can do alone, without AI, under time.
Source 5 would test what a student can do **with** AI, which is the job.

## 3. Which source speaks to which axis

This grid is the core of the rebuild. Each cell says whether that source produces evidence on
that axis today.

| Axis | Colleagues | Clients | Self | Testing center | Observed build (later) |
|---|---|---|---|---|---|
| **Builder** | | | | | |
| Discovery | Not asked | Not asked | Yes (6 items) | Yes | Yes |
| Design | Not asked | Not asked | Yes (6 items) | Yes | Yes |
| Application Architecture | Not asked | Technical competency, partly | Yes (12 items) | Yes | Yes |
| AI Systems | Not asked | Technical competency, partly | Yes (7 items) | Yes | Yes |
| Agentic Workflow | Not asked | Not asked | Yes (12 items) | Yes | Yes, its best case |
| Launch and Learn | Not asked | Not asked | Yes (7 items) | Yes | Partly |
| **Consultant** | | | | | |
| Judgment | Yes | Yes ("Their thinking") | Yes | No | Partly |
| Ownership | Yes | Yes (Timeliness, High agency) | Yes | No | No |
| Communication | Yes | Yes | Yes | No | No |
| Collaboration | Yes | Yes (Working with you, Taking feedback) | Yes | No | No |

What the grid shows:

1. **The diamond is covered from three directions.** Colleagues, clients and self all speak to
   all four axes. Nothing needs to change there.
2. **The hexagon has one outside source, and it lives in the other course.** Inside the
   Foundry Lab, the only evidence on the Builder axes is the student's own rating and the
   client's single Technical competency item. The testing-center exams are MSB 341 / IS 693R
   (Build) exams, so a student on Pathway 3 (Lab only) never sits them.
3. **Colleagues see the Builder axes and are not asked about them.** A teammate reads the
   code, the schema and the agent setup every day. That is the cheapest new evidence available.
   A proposal: add the six Builder axes to the colleague form as optional ratings, each with
   "Could not observe," anchored by stage rather than by the fifty items.
4. **The testing center cannot see the diamond, and should not try.** Exams test knowledge
   and applied reasoning. Judgment on a live client, ownership and trust are observed, not tested.
5. **The observed build is the one source that could cover the hexagon the way the job
   actually works.** The testing center deliberately removes AI. The work never does.

## 4. How feedback is gathered

Kept from v1.

**The exposure list.** Each student keeps a list in the app all semester of everyone who saw
their work: Foundry members on each engagement, anyone on an internal project, anyone who
reviewed their work. For each one: the context (which engagement or project), how they saw the
work, and the depth (Deep, Moderate, Light). The app suggests names from staffing records,
faculty approves each name and adds anyone staffing shows the student worked with. A student
reports who saw the work. Leaving someone off does not remove them.

**Clients are not on the list.** Every client contact with access to the engagement reviews every
student staffed in the block, from the client portal, at the end of each 5-week block.

**Faculty.** Scott fills in the same colleague form, when he chooses to. His rating is one more
source at the published weight; when he does not rate, the other weights scale up.

**Self-assessment.** Closes before each release, so it is always produced before the student has
seen anything. Never in the composite. Compared against it as a calibration gap, which feeds the
video reflection.

**Testing center.** Scored by the exam, reported per Builder axis on the final (15 items per
axis), so it comes back as a hexagon a student can lay over their own self-rating.

**Releases.** Responses arrive all semester. Students see results twice, at midterm and final,
combined, with an axis shown only once three different people have rated it.

## 5. When to talk and when to use the form

The two do different jobs. A conversation is for **development**: it is frequent, it is between
two people who will keep working together, and it changes the next week of work. A form is for
**the record**: it is periodic, it is combined with other people's input, and it becomes part of
a grade and a development summary.

### The rule

**Say it live before it goes on a form.** The form should never be the first place someone
hears something. This is the constitution's "no surprises" line made into a procedure: if a
colleague would be surprised by what you wrote about them, you skipped a conversation.

There is one exception, and it is the reason the form has a confidential section. Anything you
cannot safely say to the person (a conduct concern, something that made you uncomfortable,
something that fails the red face test) goes to Scott directly, or in Part E of the form, and
never through a live conversation first.

### Which to use

| Situation | Use | Why |
|---|---|---|
| Something should change this week | **Talk** | A form arrives weeks later, after the moment has passed |
| Every two weeks with your teammate | **Talk**, fifteen minutes (Appendix H) | Keeps the formal rounds free of new information |
| End of a milestone, meeting or deliverable review | **Talk**: "What is one thing I could have done better?" | The Ask First habit, at the point the work is fresh |
| Someone asked you for feedback | **Talk** | They asked; answer in the form they asked in |
| Your shared work has ended | **Form** | This is the record. It is combined with other raters and weighted by exposure |
| End of a 5-week client block | **Form** (client); Scott's 15-minute call (live counterpart) | A busy client gives five to eight minutes on a form; the call catches what the form cannot |
| You need to give a number | **Form only** | Ratings live on the form. See below |
| A conduct or safety concern | **Neither.** Go to Scott | It never travels through a survey or an informal chat |

### Talk about instances, not numbers

Live conversations should never trade ratings. A teammate who hears "I'd put you at a 3 on
Ownership" learns what one of their raters said, which undoes the three-rater floor and the
anonymity it buys. On a two-person team it also turns the form into a negotiation.

So a conversation uses the same material as the form without the scale: a specific instance,
which axis or principle it touches, and which way it missed (too little or too much). The
constitution's directional question, "which way did I miss?", is the live version of a rating.
The number goes on the form, alone.

### What this asks of each source

| Source | Live channel | Form |
|---|---|---|
| Colleagues | Biweekly fifteen minutes; Ask First after any deliverable | Colleague form when the shared work ends |
| Faculty | Studio, milestone reviews, the midterm conversation | Colleague form, optional |
| Clients | Weekly client meetings; Scott's call each block | Team review each block |
| Self | Asking others; the midterm conversation | Self-assessment before each release |
| Testing center | None | The exam |

## 6. How it becomes a grade

**Diamond: unchanged from v1.** Exposure-weighted average within each source, sources combined
per axis by the published weights (peers 40 to 50%, client 20 to 35%, faculty 25 to 30%, a
missing source reweighted), the four axes averaged equally, converted by the published table to
the Developmentship component (180 of 500 points), with the two caps (composite below 3.00 caps
the course at B; a 1 on any axis from two or more independent reviewers caps it at B-). Details
in [developmentship-model.md](developmentship-model.md), section 6.

**Hexagon: open.** The rule from v1 still holds: **demonstrated proficiency is graded and a
self-rating never is.** That rule rules out the Builder self-assessment and allows the testing
center and the observed build. What it does not settle is whether any Builder evidence enters the
Foundry Lab grade, or whether the Lab keeps grading only the diamond and reports the hexagon
alongside it. See open questions 1 to 3.

**Any change here must be published in the syllabus before the term it applies to.** The public
page today says Developmentship scores the four Consultant axes, 180 of 500 points.

## 7. Open questions

1. **Does the hexagon enter the Foundry Lab grade at all?** Option A: no, the hexagon is
   reported in the development summary and graded only in Build. Option B: yes, from outside
   sources only (testing center, colleague Builder ratings, observed build).
2. **Whose testing center?** The only proctored exams today are Build's (MSB 341 / IS 693R).
   Lab-only students (Pathway 3) never take them. Either the Lab gets its own exam, Lab students
   sit Build's final, or the testing center counts only for students enrolled in both.
3. **Should colleagues rate the Builder axes?** Cheapest new evidence, at the cost of a longer
   form (four ratings today, ten with this).
4. **The fifth source.** A timed build with AI, observed or recorded? A review of an
   agent transcript from real work? Scored by whom, against what rubric?
5. **The Claude certification.** Pearson-proctored, optional, extra credit. A sixth source on
   Agentic Workflow and AI Systems, or kept separate as a credential?
6. **Carried from v1, still unresolved:** the undergraduate conversion table, MBA internal
   leadership, discovery-only engagements, release dates, whether principle counts are shown to
   the cohort, whether the midterm release carries points.

## 8. Corrections found while assembling this draft

These are inconsistencies in the current files, independent of the rebuild.

1. `peer-evaluation-survey.md` and section 2 of `developmentship-model.md` say the principle
   dropdown holds "the ten" principles. The constitution has fourteen, and the live form
   (`PRINCIPLES` in the app's `feedback.ts`) already offers fourteen.
2. `peer-evaluation-survey.md` says stipends come from "logged, verified hours." They come from
   client weeks with utilization credit, as `developmentship-model.md` section 6 says.
3. The Google Doc "The Developmentship Model" in the team Drive (`01 Leadership & Strategy`) is
   the August 5 draft, superseded on August 12, and is still shared with seventeen people. It
   cites the old ten principles. Retire it or replace its body with a link here.

---

# Appendices

Wording below is copied from the source of truth named in each appendix. Where the live app
differs from the spec, the difference is noted.

## Appendix A. The Builder framework and its self-assessment

*Source: `website/src/lib/practice/builder.ts` (the app) and the baseline Google Form. Fifty skills under six stages. The baseline survey is the September snapshot; students update their ratings in the app after that, and re-take it in December. Never graded.*

**Scale.** 1 New to me; 2 Familiar; 3 Conversant; 4 Direct and judge; 5 Teach it.

### Discovery (6)

1. Problem vs solution: the problem, not your fix
2. User interviews: asking without leading the witness
3. Personas and segments: who it is for, who it is not
4. Competitive landscape: where the opening is
5. Prioritization: ranking by value, effort, risk
6. Spec writing: clear enough to build from

### Design (6)

1. Usability fundamentals: hierarchy, spacing, contrast, accessibility
2. User flows: mapping what the user does, step by step
3. Design direction: saying specifically what to change
4. Design systems: define a button once, not twenty times
5. UI critique: what is wrong with a generated screen
6. Prototype testing: showing a real user, then changing it

### Application Architecture (12)

1. Version control: branches, commits, and history (Git/GitHub)
2. Pull requests: review before it reaches main
3. CI: what runs automatically on every push
4. Client vs server: what runs where
5. Database schema design: tables, keys, relationships (Supabase, Postgres)
6. Auth vs authorization: who can see which rows
7. APIs: requests, responses, and why calls fail
8. Environments and secrets: why a committed key is an incident
9. Data privacy: PII, client data, what never goes in a prompt
10. Security basics: how apps leak, what a review looks for
11. Deploy, builds, and logs: machine to live app (Vercel or similar)
12. Stack selection: picking one and defending it

### AI Systems (7)

1. Context window: what fills it, what overflow does
2. Tokens, latency, and cost: what makes it slow or expensive
3. Prompt engineering: instructions, examples, structured output
4. Tool use and function calling: doing, not just saying
5. RAG: retrieval, chunking, and where retrieval fails
6. Hallucination and verification: what must be checked
7. Evals: better, not just different

### Agentic Workflow (12)

1. The agent loop: plan, act with tools, observe
2. Loop design: stopping conditions, retries, and verification gates
3. Project instructions: CLAUDE.md and repo-specific context
4. Memory: what persists across sessions
5. Skills: a workflow packaged to run the same way
6. Hooks: firing automatically on an event
7. Agent permissions: what may run unattended, what must not
8. Subagents: when parallel work helps, when it costs
9. Multi-agent orchestration: fan-out, handoffs, and merging results
10. MCP: reaching tools and data an agent lacks
11. Code review of agent output: catching what it got wrong
12. Testing AI-written code: when the model wrote the test too

### Launch and Learn (7)

1. Instrumentation: what to log before launch
2. Positioning and pricing: why someone chooses it, what it is worth
3. Metric selection: one that moves if it works
4. Activation and retention: signups are not adoption
5. Experiments: what an A/B test can prove
6. Usage analysis: deciding what to change next
7. Feature retirement: knowing when to stop


## Appendix B. The Consultant framework

*Source: `developmentship-model.md` section 3, and `PEER_ANCHORS` in the app's `feedback.ts`.*

| Axis | Judged on |
|---|---|
| Judgment | Whether they solve the right problem and say what the facts support |
| Ownership | Whether they drive the work |
| Communication | The artifacts: updates, decks, memos |
| Collaboration | Whether the team and the client trust them and want them on the next one |

#### Judgment

1. Solves the problem as handed over, even when it is the wrong one. Conclusions run ahead of
   the evidence.
2. Sound on the task in front of them, but does not ask whether it is the right task. Reports
   what the data says, not what it means.
3. Checks that the question is the right one before starting. Conclusions follow from the
   evidence, and they say where it is thin.
4. Reframes the problem when the facts call for it. Separates what is known from what is
   assumed; recommendations hold up when tested.
5. The team or client changes direction because of how they framed it. Says what the facts
   support when it is not what anyone hoped.

#### Ownership

1. Waits to be told. Work stops when the next step is unclear. Blockers surface at the
   deadline rather than before it.
2. Does assigned tasks well but does not extend past them. Asks what to do next rather than
   proposing it.
3. Owns a defined piece and finishes it. Raises blockers early. Still needs the plan handed to
   them.
4. Owns a workstream end to end. Makes the plan, unblocks themselves, and reports what they
   decided rather than asking what to do.
5. Owns a workstream and pulls others along. Reprioritizes when the client changes direction,
   and what comes back is better than what was asked for.

#### Communication

1. Updates are late or absent. The reader has to ask what happened.
2. Reports activity in the order it happened. The reader has to extract the point themselves.
3. Answer first, support underneath. Someone who reads only the first line knows the state of
   the work.
4. Writes for the specific reader. Names the decision being asked for, and the memo or deck
   holds up without anyone narrating it.
5. Produces the artifact the team reuses. A senior stakeholder can act on it without a meeting.

#### Collaboration

1. Works alone; the team and the client find out late. Takes feedback as criticism, or agrees
   and changes nothing.
2. Does their own part and reacts when asked. Leaves teammates' work and the client
   relationship to others; applies feedback only where told.
3. Reliable to work with. Keeps commitments to teammates and the client, shares context without
   being chased, and acts on feedback the next time.
4. Makes the people around them better. Asks for feedback before it is offered, says early what
   will not fit, and teammates and the client come to them directly.
5. People ask to work with them again, by name. Handles disagreement without it becoming
   personal, changes position when someone else is right, and surfaces a risk before anyone else
   finds it.

Collaboration covers everyone you work with, teammates and the client alike, and it is rated by
both. It is about the trust built over the whole engagement, so a student can be quiet in a
client meeting and still rate a 4 if the client relies on them between meetings.

## Appendix C. The constitution's fourteen principles

*Source: `students/00-constitution.qmd`, "Our four commitments". Superscripts are its scripture references.*

#### 1. Seek truth, and use it well^1^

| Principle | Too little | The golden mean | Too much |
|---|---|---|---|
| Act with integrity^2^ | Deceitful | States it plainly, including the part that costs something | Self-righteous |
| Be discerning^3^ | Repeats what was said in confidence. Says the true thing that only wounds | Tells the person who needs it, in the way they can receive it | Calls it discretion when it is avoidance |
| Be courageous^4^ | Goes along | Challenges, then commits | Fights for ego |

#### 2. Think hard and stay teachable^5^

| Principle | Too little | The golden mean | Too much |
|---|---|---|---|
| Be curious^6^ | Accepts the brief as given. Stops at the first answer | Asks the question behind the question | Chases the interesting question instead of the one that matters |
| Be rigorous^7^ | Accepts what sounds right. Trusts the output without checking the reasoning | Reasons from first principles | Rederives what is already settled. Demands proof past the point the decision needs |
| Choose humility^8^ | Defends the position instead of testing it. Ties ego to being right | Asks what they missed, then changes | Hedges. Defers when they know better |
| Seek personal improvement^9^ | Hears the feedback and files it | Asks for the critique, then acts on it | Works on themselves instead of the work. Makes every review about their growth |

#### 3. Do great work^10^

| Principle | Too little | The golden mean | Too much |
|---|---|---|---|
| Act in faith^11^ | Waits for certainty. Needs the risk gone before starting | Moves on incomplete information | Skips the preparation and calls it faith |
| Strive for excellence^12^ | Settles for what passes. Mistakes activity for achievement | Raises the bar, then clears it | Polishes past the point of value. Wields the standard to shame |
| Demonstrate high agency^13^ | Waits to be told. Explains why it was not theirs | Sees the gap and closes it | Takes what was not theirs to take. Carries it alone instead of raising it |
| Show patience^14^ | Forces the answer before it is ready. Quits when it gets hard | Presses where it can move, waits where it cannot | Waits and calls it patience. Tolerates what should have been escalated |

#### 4. Make each other better^15^

| Principle | Too little | The golden mean | Too much |
|---|---|---|---|
| Respect others^16^ | Talks past people. Dismisses the junior voice | Listens before answering | Trades candor for comfort. Plays favorites |
| Forgive quickly^17^ | Keeps score. Lets it color the next interaction | Says it once, then lets it go | Forgives before anything is named, so the pattern repeats |
| Develop others^18^ | Keeps what they know. Treats a teammate as a pair of hands | Hands it over and explains the why | Does it for them instead of with them |

## Appendix D. The colleague feedback form

*Source: `peer-evaluation-survey.md`. Filled in by every Foundry member on a student's exposure list and, optionally, by faculty, on the same form. Live at `/app/f/[token]`. Two differences in the live form: it asks for the instance under each axis rated 1, 2 or 5 rather than in two shared boxes, and its principle dropdown holds all fourteen principles where the spec says ten.*

### Part B. Reviewing each person

*One person, one context. Roughly five minutes.*

*Intro text on the form:*

> Rate against the published anchors, not against the rest of the cohort. There is no curve, so
> rating a teammate honestly costs you nothing. Rate only what you saw. "Could not observe" is a
> real answer and is better than a middling guess.

#### The four ratings

Each of the four axes is a 1 to 5 item with the full anchor text printed inline and a
**Could not observe** option.

**Judgment.** Whether they solve the right problem and say what the facts support.

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| Solves the problem as handed over, even when it is the wrong one. Conclusions run ahead of the evidence | Sound on the task in front of them, but does not ask whether it is the right task. Reports what the data says, not what it means | Checks that the question is the right one before starting. Conclusions follow from the evidence, and they say where it is thin | Reframes the problem when the facts call for it. Separates what is known from what is assumed; recommendations hold up when tested | The team or client changes direction because of how they framed it. Says what the facts support when it is not what anyone hoped |

**Ownership.** Whether they drive the work.

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| Waits to be told. Work stops when the next step is unclear. Blockers surface at the deadline | Does assigned tasks well but does not extend past them. Asks what to do next rather than proposing it | Owns a defined piece and finishes it. Raises blockers early. Still needs the plan handed to them | Owns a workstream end to end. Makes the plan, unblocks themselves, reports what they decided | Owns a workstream and pulls others along. Reprioritizes when the client changes direction, and what comes back is better than what was asked for |

**Communication.** The artifacts: updates, decks, memos.

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| Updates are late or absent. The reader has to ask what happened | Reports activity in the order it happened. The reader extracts the point themselves | Answer first, support underneath. Someone reading the first line knows the state of the work | Writes for the specific reader. Names the decision being asked for. The memo holds up without narration | Produces the artifact the team reuses. A senior stakeholder can act on it without a meeting |

**Collaboration.** Whether the team and the client trust them and want them on the next one.

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| Works alone; the team and the client find out late. Takes feedback as criticism, or agrees and changes nothing | Does their own part and reacts when asked. Leaves teammates' work and the client relationship to others; applies feedback only where told | Reliable to work with. Keeps commitments to teammates and the client, shares context without being chased, and acts on feedback the next time | Makes the people around them better. Asks for feedback before it is offered, says early what will not fit, and teammates and the client come to them directly | People ask to work with them again, by name. Handles disagreement without it becoming personal, changes position when someone else is right, and surfaces a risk before anyone else finds it |

#### The evidence questions

**Required if you gave any rating of 5.** Which axis, and what specifically did they do? One
instance is enough. *(Paragraph)*

**Required if you gave any rating of 1 or 2.** Which axis, and what specifically happened?
*(Paragraph)*

**Required of everyone.** What is the one thing this person should work on next semester?
*(Paragraph)*

> Form note: this is the most useful question here. It goes into their development summary close
> to verbatim, unattributed. Write the thing you would say to them directly, in the words you
> would use.

#### The principle citation

**Optional, and positive only.** Did you see this person live one of our principles? Which one,
and what did they do?

| Field | Type |
|---|---|
| Principle | Dropdown, the ten from the constitution. Plus "none I can point to" |
| What they did | Paragraph. Required if a principle is selected |

> Form note: this is not a rating and it does not score. Skip it if nothing comes to mind, and
> do not reach for something. **There is no negative version of this question.** You are never
> asked which principle someone failed, here or anywhere else on this form.

Two reasons it is built this way. A principle is not a thing you can rate on a scale, it is a
thing you can point at, so the form asks you to point. And an instrument that collects who
failed a value would be asking twenty-year-olds to judge each other's character for grade
weight, which is not a thing we are going to do. Failures of principle are conduct, they are
raised directly, and they never travel through a survey.

**Required of everyone.** Would you choose this person for your next engagement?

- Yes, first pick
- Yes
- Yes, with reservations
- No
- Not enough contact to say

---

### Part C. The split

*Intro text on the form:*

> Everyone can rate everyone highly. These two questions cannot be answered that way, which is
> exactly why they are here. They are confidential and never attributed.

1. **Split 100 points between you and this person,** reflecting each person's share of what
   actually got delivered. An even split is a legitimate answer if it is the true one.
2. **Did one of you carry this work?** If so, who, and what would have happened without them?
   *(Paragraph)*

Teams are two people, so the old most-want and least-want questions are gone: with one teammate
they have one possible answer.

---

### Part D. Yourself

Not here. Your self-ratings live in the [Self-Assessment Survey](self-assessment-survey.md),
which **closes before each release**.

The sequencing is deliberate. Rating yourself in the same sitting where you rate a teammate
anchors your self-rating to theirs, and the calibration gap is only meaningful if the two were
produced independently.

### Part E. Team health

*Intro text on the form:*

> Not shared with your team, and not part of anyone's grade. This is how problems reach Professor
> Murff before they become permanent.

1. Was the load fairly shared? Yes / Mostly / No
2. Did anything go wrong on this engagement that Professor Murff does not know about?
   *(Paragraph)*
3. Did anything happen on this team that made you uncomfortable? *(Paragraph)*
4. What should change about how teams are staffed next semester? *(Paragraph)*

---

## Appendix E. The client feedback forms

*Source: `client-feedback.md`. Form 2 is the one that rates students. Forms 1, 2 and 4 are live; form 3 is not built yet.*

### Form 1. Midpoint check-in

*Intro text:* "A one-minute check-in, so a problem can be fixed while there is still time."

1. How satisfied are you with the engagement so far? 1 to 5.
2. How likely are you to recommend the AI Foundry to a colleague? 0 to 10.
3. Anything we should change now? *(Optional paragraph)*

Rates no one. A 1 or 2 on question 1 puts a task on Scott's Pipeline.

---

### Form 2. Team review

*Intro text:* "A few questions about each student on your team for the last five weeks. Rate
only what you saw. 'Not enough contact to say' is a useful answer. Students see these only
combined with other people's ratings, never with your name on them."

#### Per student (repeats for each student staffed in the block)

**1. Timeliness.** Did they do what they said, when they said?

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| Missed commitments without warning | Often late, usually told us | Mostly on time | Consistently on time, and told us early when something would slip | We never had to ask where something was |

**2. Communication.** Could you act on what they sent you without them in the room?

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| Had to ask what it meant | Had to dig for the point | Clear, we knew where things stood | Written for us specifically, named the decision we had to make | We reused it internally |

**3. High agency.** Did they move the work forward on their own?

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| Waited to be told at every step | Did what was asked, nothing more | Owned their piece once it was scoped | Proposed the next step before we did | Saw what needed doing and did it before we noticed |

**4. Technical competency.** Does what they built work?

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| Did not work | Worked in a demo, not in our environment | Works, with known gaps | Works in our environment, and we understand how | Our own people can run and extend it without them |

*Plus:* Not my area to judge

**5. Contribution.** Was their work worth having?

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| We would not want it again | Below what we expected | About what we expected | Better than we expected | It changed a decision we were going to make anyway |

**6. Judgment.** Did their thinking hold up?

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| Their recommendations did not hold up | Did what we asked without questioning whether it was the right thing | Sound, and told us where the evidence was thin | Told us what the facts supported, even when it was not what we hoped | Reframed the problem in a way that changed what we asked for |

**7. Working with you.** How was this person to work with, and did you come to trust them?

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| We could not rely on them | Responsive when asked, did not go further | Reliable: did what they said, when they said | Understood what we needed and told us early what would not fit | We would ask for this person by name and bring them our next problem |

**8. Taking feedback.** When you pushed back or asked for changes, how did they respond?

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| Got defensive, or agreed and changed nothing | Changed only what we spelled out | Took it in, and the next piece showed it | Asked for our view before we offered it | Disagreed with us openly when they had reason, and changed position when we were right |

Every item from 1 to 8 also offers "Not enough contact to say."

**9. Required, one sentence each.** One thing this person did well. One thing they should work
on.

**10. Would you want this person on your next engagement?** Yes, specifically / Yes / Yes, with
reservations / No / Not enough contact to say.

#### About the team (once)

**11. Did anything the team told you turn out to be more optimistic than reality?** What was it,
and how did you find out? *(Optional paragraph)*

**12. Did anyone on the team do something that stuck with you?** It does not have to be about
the deliverable. *(Optional paragraph)* Our principle citation, asked in plain language; tagged
to a principle on our side. Positive-only by construction.

---

### Form 3. Final review

Sent with form 2 at the end of the engagement's last block. *Intro text:* "This part is about the
engagement and the program, not any student. It is never shared with students."

1. How satisfied are you with the engagement? 1 to 5.
2. How likely are you to recommend the AI Foundry to a colleague? 0 to 10.
3. **Value against the fees.** Well below / somewhat below / about equal / somewhat above / well
   above.
4. **Your own time.** How much of your team's time did this take? Far more than expected /
   somewhat more / about what we expected / less.
5. **Team size.** For work like yours: fewer students / the same / one more / substantially
   larger.
6. **Would you work with the Foundry again?** Yes, already planning it / Yes, likely / Maybe,
   depends on the scope / No.
7. **Would you refer us?** Yes / Maybe / No. If yes, who should we talk to?
8. **When you needed something, did you go to a particular person or to the group?** Who, and
   why them? *(Optional)*
9. **Was there a moment someone told you something you did not want to hear?** What happened
   after? *(Optional)*
10. **Anything else about the engagement, the fees, or the program?** *(Optional paragraph)*

Questions 8 and 9 come from the old Section 3. They feed the professor's evidence, not a score.

---

### Form 4. Feedback to Scott

Anytime, from the portal. *Intro text:* "How AI Foundry's faculty has run your engagement. Read
by Scott Murff, so it is not anonymous."

1. How responsive has AI Foundry been when you needed something? 1 to 5.
2. Did staffing put the right students on your work? Yes / Mostly / No. *(Optional comment)*
3. Were the agreement and billing clear? Yes / Mostly / No. *(Optional comment)*
4. What should Scott do differently? *(Paragraph)*

Never shared with students; never enters a grade.

---

## Appendix F. The Consultant self-assessment

*Source: `self-assessment-survey.md`. Closes before each release. Never in the composite. The Builder self-assessment is the fifty items in Appendix A.*

### Section 0. About you

| Question | Type |
|---|---|
| Your name, engagements, and internal projects | Filled in from the Cockpit |
| Which release is this for? | Filled in: midterm or final |

---

### Section 1. Your four ratings

*Intro text on the form:*

> Rate yourself against the same anchors everyone else is using. They are printed below each
> question. Nobody's grade moves because of what you put here, in either direction. What moves is
> how well you know yourself, which is measured later, by comparing this to what came back.

Four items, 1 to 5, full anchor text printed inline, identical wording to the peer form:

- **Judgment**
- **Ownership**
- **Communication**
- **Collaboration**

**No "could not observe" option.** You were there for all of it.

---

### Section 2. Your evidence

*Intro text on the form:*

> One paragraph each. Point at something that happened. If you cannot name an instance, that is
> the most useful thing this form will tell you, and the honest answer is to say so.

Each question is the same underlying question the other two forms ask, turned around to face you.

| # | Question | Axis |
|---|---|---|
| 1 | **Point to a decision where your framing or your reading of the facts changed what the team or client did.** What did you see that others had not? | Judgment |
| 2 | **Was there something the team or the client needed to hear that they would not like?** Who said it, and what happened? | Judgment |
| 3 | **What did you own end to end this semester** that nobody had to chase you about? Who decided what the steps were? | Ownership |
| 4 | **When did the work get stuck, and what did you do next?** How did your teammate find out, and when? | Ownership |
| 5 | **Point to one thing you wrote that someone acted on** without needing you in the room. | Communication |
| 6 | **When something was going badly, how did the client and your teammate hear about it?** From you, from someone else, or from the result? | Communication |
| 7 | **How did you earn the trust of your team and your client?** What did you do, and how could you tell it worked? | Collaboration |
| 8 | **What is the last correction you received, from a teammate or the client, and what changed in the next piece of work?** | Collaboration |

**9. Which principle did you live this semester, and what did you do?** Pick one from the
constitution and point at something specific. *(Dropdown plus paragraph. Positive only. You are
not asked which principle you failed, and neither is anyone else.)*

Questions 2, 4, 6 and 8 are the ones that produce honest answers, because they ask about a specific
event with a specific outcome rather than asking you to characterize yourself.

---

### Section 3. Prediction

*Intro text on the form:*

> Before you see any of it. This is the only part of the form where being right counts for
> anything, and it counts in your video reflection, not in your ratings.

1. **On which axis do you expect your reviewers to rate you highest?** Why? *(Paragraph)*
2. **On which axis do you expect them to rate you lowest?** Why? *(Paragraph)*
3. **What is the one criticism you expect to see,** stated the way you think they will state it?
   *(Paragraph)*
4. **Which of the people on your exposure list do you think would pick you first for their next
   engagement, and who would not?** *(Paragraph. Never shared with anyone named.)*

Question 3 is the highest-value item on this form. A student who can write their own criticism
before reading it has already done the developmental work, and a student who cannot has told us
where to spend the conversation.

---

### Section 4. Forward

1. **What is the one thing you are working on next semester?** *(Paragraph)*
2. **What would have to be true for you to move one full point on your lowest axis?**
   *(Paragraph)*
3. **What do you need from the Foundry that you are not getting?** *(Paragraph. Read by faculty
   only.)*

---
## Appendix G. The exams

*Sources: `~/courses/product-management/00-assessments.qmd` and `index.qmd` (Build, Fall 2026),
and `students/08-certification.qmd` (this course).*

| Exam | Course | Where | When (Fall 2026) | Items | Covers | Weight |
|---|---|---|---|---|---|---|
| **Build midterm** | MSB 341 / IS 693R | BYU Testing Center, proctored, closed book, no AI | Tue Oct 20 to Thu Oct 22 | 40 | Classes 1 to 6: Agentic Workflow, Discovery, Design | 25 of 500 (5%) |
| **Build final** | MSB 341 / IS 693R | BYU Testing Center, proctored, closed book, no AI | Tue Dec 8 to Wed Dec 9 | 90, 15 per Builder axis | All six Builder axes, cumulative | 25 of 500 (5%) |
| **Claude Certified Developer, Foundations** | AI Foundry (certification track) | Online proctored or a Pearson test center | Student schedules; prep runs weeks 1 to 14 | Multiple choice and scenario-based, 120 minutes | Claude API, Claude Code, MCP: mostly AI Systems and Agentic Workflow | Optional. Passing is extra credit; failing costs nothing |

The Build final is the one built to be a source for this model. Because every axis has fifteen
items, its score comes back as a hexagon that lays directly over the Builder self-assessment.
The Build course's own words: "The gap between what you think you know and what you can produce
under proctoring is usually the most useful thing on the page." Its items are application, not
recall ("which of these is a leading indicator for this product," not "define leading
indicator").

The Lab has no testing-center exam of its own. See open question 2.

The certification track's four required deliverables (an evaluation harness, a Skill with hooks,
an MCP server against a real system, and a written answer to the mock exam's weakest domain) are
already hands-on builds reviewed at studio. They are the nearest existing thing to source 5.

## Appendix H. Giving feedback in a live conversation

*New in this draft. For any two Foundry members, a member and faculty, or a member and a client.
Draws on the constitution's Ask First culture and its golden mean.*

### When

Fifteen minutes every two weeks with your teammate, and at the end of any milestone, meeting or
deliverable review. Also any time someone asks. The person who wants feedback asks for it;
waiting to be told is the failure the Ask First culture exists to remove.

### Before

Each of you brings **one** instance for the other: a specific thing that happened in the last
two weeks, with a date or an artifact you can point to. One instance discussed well does more
than five listed. If you cannot think of one, bring a question instead ("I wasn't sure whether
you wanted me to take the schema; did I wait too long?").

Bring something that went well, too, and be as specific about it as about the problem. "The
Thursday memo named the decision Brian had to make, and he made it on the call" tells a person
what to repeat. "Good job this week" does not.

### The conversation

1. **The receiver asks.** "What is one thing I could have done better in the last two weeks?"
   Then the directional question from the constitution: "Which way did I miss: too little, or
   too much?"
2. **The giver names the instance.** What happened, when, and what you saw. Describe the
   behavior, not the person: "You pushed the fix Tuesday night without telling the client the
   demo would change" rather than "You don't communicate."
3. **The giver says what it affected.** On the work, the client, or you. "Brian opened the demo
   Wednesday and thought it was broken."
4. **The giver says which way it missed.** Use the constitution's language where it fits:
   "On high agency I think you were on the too-much side here: you closed a gap that was the
   client's to decide." Name the axis or the principle if it helps; skip it if it doesn't.
5. **The giver says what would look different next time.** One concrete thing.
6. **The receiver restates it, asks at most one question, and does not defend.** "So the fix
   was fine; the problem was that Brian found it before I told him. Next time a change touches
   what the client sees, I send a line first." Explaining why it happened is fine later; in this
   moment it reads as a defense and the giver stops talking.
7. **Swap.**
8. **Close.** Each person says the one thing they will do differently before the next
   conversation. Start the next one by asking whether it happened.

### Rules

- **Instances, not traits.** "Tell me about a time" produces something to act on. "You're a
  great communicator" produces an adjective.
- **No numbers.** Never say where you would rate someone. Ratings go on the form, alone,
  combined with other people's (section 5).
- **Private, and in a way they can receive it** (Be discerning). Not in front of the client,
  not in the team channel.
- **Say it once, then let it go** (Forgive quickly). The next conversation starts fresh.
- **If you are giving it to someone more senior,** including faculty, the same steps apply.
  Feedback flows in every direction.
- **If it is a conduct concern,** this is the wrong place. Go to Scott.

### With a client

At the end of each block, ask the client directly: "What should we do differently in the next
five weeks?" and "Was there anything we told you that turned out more optimistic than it
should have been?" Write down what they say and tell your teammate the same day. Their answers
on the team review form should not surprise you.

### The professor's interview guide

*Kept from v1 (`developmentship-model.md` section 5). Used only in the four cases where the
professor interviews a reviewer: every client once per round, material disagreement between
sources, a composite within 0.25 of a cap, or on request.*

#### Opening

> This is confidential. Nothing you say gets attributed to you, and what comes back to them is a
> summary of themes across everyone who worked with them. I am going to ask about specific
> things that happened, not for an overall impression. If you cannot remember an instance, say
> so, that is a useful answer too.

The last sentence matters. It gives permission for "I never saw that," which is what keeps a
reviewer from inventing a middling answer to be polite.

#### Judgment

1. **Was there a point where they asked whether the team was solving the right problem?** What
   prompted it, and what happened next?
2. **Think of a recommendation they made, or a conclusion they drew from data.** Did it hold up?
   Did they say where the evidence was thin? Was there something the client needed to hear that
   they would not like, and who said it?

*Listening for: whether the framing came from them or was handed to them. Whether conclusions
stayed inside the evidence. Whether an unwelcome finding was stated plainly or softened away.*

#### Ownership

3. **What did they own?** Walk me through a piece of work that was theirs end to end. Who
   decided what the steps were?
4. **Tell me about a time the work got stuck.** How did you find out? What did they do next?
5. **When the client changed direction or a deadline moved,** what did they do without being
   asked? If they committed to something in a client meeting, did it happen when they said?

*Listening for: whether the plan came from them or was handed to them. Whether blockers arrived
early or at the deadline. Whether "not my job" ever appeared in any form.*

#### Communication

6. **Think of something they wrote, an update, a memo, a deck.** Could you tell the state of the
   work from the first few lines, or did you have to dig? Did you need them in the room for it to
   make sense?
7. **When something was going badly, how did you hear about it?** From them, from someone else,
   or from the result?

*Listening for: answer first versus activity log. Whether bad news traveled at the same speed as
good news.*

#### Collaboration

8. **Would you staff them on your next project?** Why, specifically?
9. **How did the client's trust in them change over the engagement?** What did they do that
   earned it, or cost it? Did the client start coming to them directly?
10. **Tell me about a disagreement, on the team or with the client.** What was their part in it,
    and how did it end?
11. **When was the last time they changed their mind because of something a teammate or the
    client said?** What happened when someone gave them a correction?

*Listening for: whether the disagreement stayed about the work. Whether feedback produced a
visible change in the next piece of work or just a pleasant nod. Whether the client's interest
came ahead of looking good.*

#### Closing

12. **What is the one thing they should work on next semester?**
13. **Is there anything I did not ask about that I should know?**
14. **Who else saw their work closely?**

Question 12 is the most valuable one in the guide, because it is the sentence that goes into the
development summary almost verbatim. It is also question 3 of the peer form, which is why the
form can substitute for the interview in most cases. Question 14 validates the exposure list
against reality.

#### The client call

Runs against [Client Feedback](client-feedback.md) rather than this guide. Its event questions
are the interview: what the team was optimistic about, who the client went to when they needed
something, and what hard thing got said. Fifteen minutes, and it doubles as
a relationship call.

#### Rules for the professor

- **Ask for an instance, not a trait.** "Tell me about a time" produces evidence. "Are they a
  good communicator" produces an adjective.
- **Follow the story, not the script.** These are the questions that must get answered, not the
  order they must be answered in.
- **Push once on a generality, then let it go.** A second push produces a manufactured example,
  which is worse than no example.
- **Do not defend the student.** The reviewer stops talking.
- **Write the rating within the hour.** Not during, not the next day.
