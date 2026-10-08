# Client Feedback

*Internal spec. Source of truth for every form an AI Foundry client fills in: in the client
portal (aifoundry.byu.edu/app, Give feedback) and through the private link `/app/f/[token]` for
contacts without an account. Replaces `client-evaluation-survey.md` (2026-10-08).*

Status: **drafted, not built.** The live form implements an earlier version; the gaps are listed
at the end.

## The four forms

| Form | When | Who gets it | Rates people? | Read by | Time |
|---|---|---|---|---|---|
| 1. Midpoint check-in | Week 3 of the first 5-week block only | The sponsor | No | Scott | 1 min |
| 2. Team review | End of every 5-week block | Every client contact on a student's exposure list for that block | Yes, each student | Feeds the diamond and the grade (see below) | 5 to 8 min |
| 3. Final review | The engagement's last block only, with form 2 | The sponsor | No | Scott; never students | 5 min |
| 4. Feedback to Scott | Anytime | Any client contact | Scott | Scott | As long as they like |

A client fills in at most two forms at once (2 and 3, at the very end), and form 2 covers every
student in one sitting.

## Design rules

- **Ask only what the client saw.** A client sees deadlines, what lands in their inbox, whether
  a recommendation held up, whether they came to trust someone, how a person took pushback,
  whether a person proposed the next step, and whether the thing works in their environment.
  They rarely see who drove the work inside the team or how teammates treat each other. So the
  client form asks about the outside of the work and the client's side of the relationship; the
  [peer form](peer-evaluation-survey.md) asks about the inside. Between them, all four axes are
  rated by both.
- **The same five questions as STRAT 477R.** Timeliness, Communication, High Agency, Technical
  Competency and Contribution are what any supervisor-type rater can see, and they are the APM
  Lab mentor survey's five (`~/courses/apm-lab/partners/03-evaluation.qmd`). Using them here
  gives one question set for mentors and clients. The Foundry adds three questions 477R does not
  ask: whether their thinking held up (Judgment), how they were to work with, and how they
  responded to pushback (both Collaboration). These three feed the diamond only, never the
  Client Evaluation grade.
- **Per student, no separate team section.** Teams are one or two students, so rating each
  costs the client little. A team score, where one is needed, is the average of its students.
- **The client never sees the framework.** No axis names, no diamond, no anchors framed as a
  rubric. The anchors on this form are plain descriptions of what happened. The mapping to the
  diamond happens on our side.
- **Every rating has an escape.** "Not enough contact to say" on every per-student rating, and
  "Not my area to judge" on Technical Competency. A blank is worth more than a guess.
- **1 to 5 on every rating,** matching the diamond, with five written anchors. The one exception
  is likelihood to recommend, 0 to 10, the standard form of that question.
- **Events beat opinions.** "Did anything turn out more optimistic than reality" gets an honest
  answer because it asks about an event.
- **Program questions are never shared with students,** which is what keeps them honest.

---

## Form 1. Midpoint check-in

*Intro text:* "A one-minute check-in, so a problem can be fixed while there is still time."

1. How satisfied are you with the engagement so far? 1 to 5.
2. How likely are you to recommend the AI Foundry to a colleague? 0 to 10.
3. Anything we should change now? *(Optional paragraph)*

Rates no one. A 1 or 2 on question 1 puts a task on Scott's Pipeline.

---

## Form 2. Team review

*Intro text:* "A few questions about each student on your team for the last five weeks. Rate
only what you saw. 'Not enough contact to say' is a useful answer. Students see these only
combined with other people's ratings, never with your name on them."

### Per student (repeats for each student staffed in the block)

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

### About the team (once)

**11. Did anything the team told you turn out to be more optimistic than reality?** What was it,
and how did you find out? *(Optional paragraph)*

**12. Did anyone on the team do something that stuck with you?** It does not have to be about
the deliverable. *(Optional paragraph)* Our principle citation, asked in plain language; tagged
to a principle on our side. Positive-only by construction.

---

## Form 3. Final review

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

## Form 4. Feedback to Scott

Anytime, from the portal. *Intro text:* "How AI Foundry's faculty has run your engagement. Read
by Scott Murff, so it is not anonymous."

1. How responsive has AI Foundry been when you needed something? 1 to 5.
2. Did staffing put the right students on your work? Yes / Mostly / No. *(Optional comment)*
3. Were the agreement and billing clear? Yes / Mostly / No. *(Optional comment)*
4. What should Scott do differently? *(Paragraph)*

Never shared with students; never enters a grade.

---

## Where each answer goes

| Item | Diamond (consultant) | Client Evaluation grade | Other |
|---|---|---|---|
| 2.1 Timeliness | Ownership, half of the client source | Yes | |
| 2.2 Communication | Communication | Yes | |
| 2.3 High agency | Ownership, half of the client source | Yes | |
| 2.4 Technical competency | No | Yes | Shown beside the builder chart as an outside view, never blended into it |
| 2.5 Contribution | No | Yes | |
| 2.6 Judgment | Judgment | No | |
| 2.7 Working with you | Collaboration, half of the client source | No | |
| 2.8 Taking feedback | Collaboration, half of the client source | No | |
| 2.9 Did well / work on | No | No | Development summary, quoted unattributed |
| 2.10 Next engagement | No | No | Triangulation: a "No" against high peer ratings is worth a conversation |
| 2.11 Optimistic | No | No | Evidence the professor weighs when sources disagree |
| 2.12 Stuck with you | No | No | Principle tag; development summary only |
| Forms 1 and 3 | No | No | Program, pricing and renewal decisions; satisfaction and recommend tracked per engagement on the Pipeline |
| Form 4 | No | No | Scott only |

### Diamond mechanics

- **Client source per axis, per student:** Judgment = item 6. Ownership = mean of the usable
  Timeliness and High Agency ratings, counted as one response. Communication = item 2.
  Collaboration = mean of the usable Working with you and Taking feedback ratings, counted as
  one response. Clients rate all four axes.
- **Weights** (`WEIGHTS` in `consultant.ts`), peer, client, faculty: Judgment 0.4, 0.3, 0.3;
  Ownership 0.5, 0.2, 0.3; Communication 0.4, 0.35, 0.25; Collaboration 0.4, 0.35, 0.25. A
  missing source is reweighted, not zeroed. The client is a minor source for Ownership, because
  a teammate sees ownership from inside, and a near-equal one for Communication and
  Collaboration, where the client is the reader and the other half of the relationship.
- **Team of one:** no peer is on the engagement, so the peer source is often empty and the
  formula reweights. The client then carries every axis, with faculty if Scott rated (optional). Intended.
- **Repeat ratings:** a client who rates a student at the end of three blocks is still one rater
  toward the three-rater minimum (`raterKey`). Their ratings are averaged per rater first, so a
  client with three blocks weighs the same as a client with one.
- **Release rules unchanged:** students see the diamond only at the midterm and final releases,
  an axis only with three or more raters, never attributed.

### Grade mechanics

The syllabus (`students/01-syllabus.qmd`, Client Evaluation, 64 points) says the client rates
the **team** on these five dimensions, at mid-term for development and at the end for the grade,
and the average converts to points. This spec keeps that rule exactly: the graded number is the
team average of items 2.1 to 2.5 across its students, from the reviews that end in the term.
Per-student scores are collected now so the rule can change later. Any change to per-student
grading must be published in the syllabus before the term it applies to. Items 2.6 to 2.8
(Judgment, Working with you, Taking feedback) never enter the grade.

---

## What changes in the app (strategy repo)

- `CLIENT_QUESTIONS` (`src/lib/practice/feedback.ts`): eight rated per-student items with the
  anchors above, plus the escape options.
- `FeedbackResponse`: add timeliness, agency, technical, contribution, judgment, taking
  feedback. Ownership and Collaboration for a client are derived, not stored.
- `consultant.ts`: the four axes are Judgment, Ownership, Communication, Collaboration (Client
  Hands removed, Workstream Ownership renamed); new `WEIGHTS` as above; client Ownership from
  Timeliness and High Agency, client Collaboration from Working with you and Taking feedback;
  per-rater averaging before the client source mean.
- Requests per 5-week block: `feedback_requests.block`, ready when the block ends, not when the
  student's last stint ends (today's `workEnded`).
- `/app/f/[token]` form: render form 2 (and form 3 on the last block).
- New in the portal: forms 1, 3 and 4.
- Builder chart: show the client's Technical Competency beside it.

## What the live form asks today

Live at `/app/f/[token]` (2026-10-08): per student, the old A (working with you), B (what they
sent you), C (ownership, optional), one thing done well and one to work on, next engagement;
then satisfaction, recommend, optimistic, and stuck with you. Missing from it: Timeliness, High
Agency, Technical Competency, Contribution, Judgment and Taking feedback, which means the Client Evaluation grade
component has no data source today; and all of form 3 beyond the two scores.

## Open decisions

1. **Letter grade.** The old Section 4 asked the client for a letter grade "Professor Murff
   welcomes." Dropped here. Bring it back only as an input the professor may weigh, never a
   formula.
2. **477R mentors.** Whether they move to these anchored versions of the same five, so both
   programs use one form.
3. **Technical Competency and the builder chart.** Shown beside it as proposed, or not at all.
4. **Which reviews count for the grade** when an engagement spans the end of the term.

## Change log

- 2026-10-08: rewritten from `client-evaluation-survey.md`. Five 477R items plus "working with
  you," per student, at the end of every 5-week block; team section folded into per-student
  ratings; four forms (midpoint, team review, final review, Scott); program questions moved to
  the final review only; scale rule stated with its one exception; question counts fixed;
  "builders" and "Cockpit" replaced.
- 2026-10-08: Consultant diamond recut to Judgment, Ownership, Communication, Collaboration.
  Added per-student items Judgment (2.6) and Taking feedback (2.8); High Agency anchor 5
  changed to "Saw what needed doing and did it before we noticed" (its old text moved to
  Judgment); Working with you now feeds Collaboration, averaged with Taking feedback; clients
  now rate all four axes; items renumbered; new weights.
