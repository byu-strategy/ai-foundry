#!/usr/bin/env python3
"""Plan (and, only with --apply, create) the fall sprint assignments in Canvas course 37925.

AI Foundry, MBA 693R-011 cross-listed with STRAT 490R-001. The rules come from the published
Sprints page (students/11-sprints.qmd) and the syllabus Grading section (students/01-syllabus.qmd):

    3 sprints x (Plan 10 + Wrap-up 110) = 360
    Colleague and client feedback         140
    Total                                 500
    Extra credit: student ratings 10, weekly updates 2 each for Sep 14 to Oct 12 (max 10)

Setup mirrors MSB 341 (Canvas 36977): one unweighted "Assignments" group, online_text_entry
link submissions, points grading, the late policy set on the course (10% per day, no floor), and
manual grade posting so scores stay hidden until released.

Usage:
    python3 scripts/create_sprint_assignments.py            # dry run (default): GETs only
    python3 scripts/create_sprint_assignments.py --apply    # creates in Canvas, then reads back

Dry run sends GET requests only. Apply is idempotent by name: anything already present is left
alone and reported. The script holds no secrets and no student data; the Canvas token is read
from ~/hubs/courses/.env.local at run time and never printed.

Due dates go through canvas_due.due() (America/Denver via zoneinfo), never CANVAS_TZ_OFFSET:
the Nov 1 DST change falls inside Sprint 1.
"""
import argparse
import datetime as dt
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path.home() / "courses/product-management/scripts"))
from canvas_due import due, local  # noqa: E402  (imported, never edited: MSB 341 is locked)

COURSE_ID = 37925
ENV_FILE = Path.home() / "hubs/courses/.env.local"
TZ = ZoneInfo("America/Denver")

SITE = "https://byu-strategy.github.io/ai-foundry/students"
SPRINTS_PAGE = f"{SITE}/11-sprints.html"
SYLLABUS = f"{SITE}/01-syllabus.html"

LATE_DAYS = 9               # "accepted up to 9 days late"
LATE_POLICY = {             # same as 36977's late policy
    "late_submission_deduction_enabled": True,
    "late_submission_deduction": 10.0,
    "late_submission_interval": "day",
    "late_submission_minimum_percent_enabled": False,
    "missing_submission_deduction_enabled": False,
}

MAIN_GROUP = "Assignments"   # exists in 37925 already (unweighted), as in 36977
EC_GROUP = "Extra credit"

# Sprint calendar, course-local time. Plans are due 11:59 PM; Wrap-ups at 8:00 AM studio start.
SPRINTS = [
    (1, "2026-10-26 23:59", "2026-11-06 08:00"),
    (2, "2026-11-09 23:59", "2026-11-20 08:00"),
    (3, "2026-11-23 23:59", "2026-12-04 08:00"),
]


def fmt_local(local_str):
    d = dt.datetime.strptime(local_str, "%Y-%m-%d %H:%M")
    return d.strftime("%A, %B %-d at %-I:%M %p")


def lock_after(local_str, days=LATE_DAYS):
    """Exactly `days` x 24 hours after the due time, as UTC for Canvas.

    Elapsed time, not wall-clock time: Canvas counts days late by elapsed time, so a lock set on
    the wall clock across the Nov 1 time change would leave an hour that scores 0.
    """
    d = dt.datetime.fromisoformat(due(local_str).replace("Z", "+00:00")) + dt.timedelta(days=days)
    return d.astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def plan_description(n, due_local):
    return f"""<p><strong>Your Sprint {n} plan is due {fmt_local(due_local)}.</strong> 10 points, graded
for completion: on time, with every field filled in, earns all 10. Your predicted difficulty is not graded.</p>
<h3>To submit</h3>
<ol>
<li>Run <code>/sprint-plan</code> in your Foundry repo. It writes <code>sprints/sprint-{n}-plan.md</code>. Commit and push it.</li>
<li><strong>Paste the GitHub link to your plan file here.</strong> Open <code>sprints/sprint-{n}-plan.md</code> on github.com and copy the URL, for example:
<pre>https://github.com/your-username/your-netid_foundry/blob/main/sprints/sprint-{n}-plan.md</pre></li>
</ol>
<p><strong>You can change the plan during the sprint.</strong> Run <code>/sprint-plan</code> again. It asks what is
changing and why, updates the plan with a dated note, and commits it. You do not resubmit here: the link
always shows the current file.</p>
<p>Late work loses 10% per day, applied by Canvas, and is accepted up to 9 days late.</p>
<p><a href="{SPRINTS_PAGE}#the-plan"><strong>The plan, on the Sprints page</strong></a></p>"""


def wrapup_description(n, due_local):
    return f"""<p><strong>Sprint {n} Wrap-up is due {fmt_local(due_local)}, when studio starts.</strong>
110 points: Output 60, Review 25, Demo 25. See the
<a href="{SPRINTS_PAGE}#grading-rubric">rubric</a>.</p>
<h3>What you need by the due date</h3>
<ul>
<li>Your output: your part of the plan, real, finished, and checkable. List every place it lives under
<strong>Where the work lives</strong> in your README. See <a href="{SPRINTS_PAGE}#what-counts-as-build-output">Build output</a>
and <a href="{SPRINTS_PAGE}#what-counts-as-learn-output">Learn output</a>.</li>
<li>Your review, <code>sprints/sprint-{n}-review.md</code>: run <code>/sprint-review</code>, answer its six retro
questions, and commit and push the file. See <a href="{SPRINTS_PAGE}#the-review">The review</a>.</li>
<li>A 2 to 3 minute demo on Loom of your work, working. Loom only: a demo on Google Drive, YouTube, or an
uploaded file scores 0. See <a href="{SPRINTS_PAGE}#the-demo">The demo</a>.</li>
</ul>
<h3>To submit</h3>
<p>Paste two links here:</p>
<ol>
<li><strong>Your review file on GitHub.</strong> Open <code>sprints/sprint-{n}-review.md</code> on github.com and copy the URL, for example:
<pre>https://github.com/your-username/your-netid_foundry/blob/main/sprints/sprint-{n}-review.md</pre></li>
<li><strong>Your Loom share link</strong> (loom.com/share/...), set to "Anyone with the link" or shared with scott.murff@byu.edu.</li>
</ol>
<p>Late work loses 10% per day, applied by Canvas, and is accepted up to 9 days late.</p>
<p><a href="{SPRINTS_PAGE}#the-wrap-up"><strong>The Wrap-up, on the Sprints page</strong></a></p>"""


FEEDBACK_DESC = f"""<p>140 points. Your colleagues and your clients rate you on the four Consultant axes:
Judgment, Ownership, Communication, and Collaboration. The fall round runs from November 20 to December 14.
There is nothing to submit here.</p>
<p><a href="{SYLLABUS}#grading"><strong>Grading, in the syllabus</strong></a></p>"""

RATINGS_DESC = f"""<p>Extra credit, up to 10 points. Complete the BYU end-of-semester student ratings survey.
There is nothing to submit here. This adds points to your grade without adding to the 500-point total.</p>
<p><a href="{SYLLABUS}#extra-credit"><strong>Extra credit, in the syllabus</strong></a></p>"""

UPDATES_DESC = f"""<p>Extra credit, 2 points for each weekly update you sent for the weeks of September 14
through October 12, up to 10 points. There is nothing to submit here. This adds points to your grade without
adding to the 500-point total.</p>
<p><a href="{SYLLABUS}#extra-credit"><strong>Extra credit, in the syllabus</strong></a></p>"""


def build_plan():
    """Every assignment, in module order. Pure data: no Canvas calls."""
    items = []
    for n, plan_due, wrap_due in SPRINTS:
        items.append(dict(
            name=f"Sprint {n} Plan", group=MAIN_GROUP, points_possible=10,
            due_local=plan_due, due_at=due(plan_due), lock_at=None,
            submission_types=["online_text_entry"], published=True, in_module=True,
            description=plan_description(n, plan_due)))
        items.append(dict(
            name=f"Sprint {n} Wrap-up", group=MAIN_GROUP, points_possible=110,
            due_local=wrap_due, due_at=due(wrap_due), lock_at=None,
            submission_types=["online_text_entry"], published=True, in_module=True,
            description=wrapup_description(n, wrap_due)))
    items.append(dict(
        name="Colleague and client feedback", group=MAIN_GROUP, points_possible=140,
        due_local="2026-12-14 23:59", due_at=due("2026-12-14 23:59"), lock_at=None,
        submission_types=["none"], published=False, in_module=False, description=FEEDBACK_DESC))
    # Extra credit: 0-point assignments, scored above zero. Groups are unweighted, so the course
    # total is the sum of points earned over the sum of points possible; a 0-point assignment adds
    # to the first and not the second. No due date and no submission, so the late policy never
    # touches them and nobody shows as missing.
    items.append(dict(
        name="Extra credit: student ratings", group=EC_GROUP, points_possible=0,
        due_local=None, due_at=None, lock_at=None,
        submission_types=["none"], published=True, in_module=False, description=RATINGS_DESC))
    items.append(dict(
        name="Extra credit: weekly updates (Sep 14 to Oct 12)", group=EC_GROUP, points_possible=0,
        due_local=None, due_at=None, lock_at=None,
        submission_types=["none"], published=True, in_module=False, description=UPDATES_DESC))
    for i in items:
        i.update(grading_type="points", omit_from_final_grade=False, post_manually=True)
    return items


# --- Canvas ---------------------------------------------------------------------------------

def load_env():
    env = {}
    for line in ENV_FILE.read_text().splitlines():
        m = re.match(r"^(CANVAS_API_(?:TOKEN|URL))=(.*)$", line.strip())
        if m:
            env[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    if "CANVAS_API_TOKEN" not in env or "CANVAS_API_URL" not in env:
        sys.exit(f"CANVAS_API_TOKEN / CANVAS_API_URL not found in {ENV_FILE}")
    base = env["CANVAS_API_URL"].rstrip("/")
    if not base.endswith("/api/v1"):
        base += "/api/v1"
    return base, env["CANVAS_API_TOKEN"]


class Canvas:
    def __init__(self, allow_writes):
        self.base, self._token = load_env()
        self.allow_writes = allow_writes

    def _req(self, method, path, body=None):
        if method != "GET" and not self.allow_writes:
            raise RuntimeError(f"refusing {method} {path}: dry run")
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(self.base + path, data=data, method=method, headers={
            "Authorization": f"Bearer {self._token}", "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req) as r:
                return r.status, json.load(r)
        except urllib.error.HTTPError as e:
            return e.code, None

    def graphql(self, query):
        if not self.allow_writes:
            raise RuntimeError("refusing GraphQL mutation: dry run")
        req = urllib.request.Request(self.base[: -len("/v1")] + "/graphql",
                                     data=json.dumps({"query": query}).encode(), method="POST",
                                     headers={"Authorization": f"Bearer {self._token}",
                                              "Content-Type": "application/json"})
        with urllib.request.urlopen(req) as r:
            out = json.load(r)
        errs = [e for v in (out.get("data") or {}).values() if v for e in (v.get("errors") or [])]
        if out.get("errors") or errs:
            sys.exit(f"GraphQL failed: {out.get('errors') or errs}")
        return out

    def get(self, path):
        status, out = self._req("GET", path)
        return out if status == 200 else None

    def get_all(self, path):
        sep = "&" if "?" in path else "?"
        return self.get(f"{path}{sep}per_page=100") or []

    def write(self, method, path, body):
        status, out = self._req(method, path, body)
        if status not in (200, 201):
            sys.exit(f"{method} {path} failed with HTTP {status}")
        return out


def show_local(utc):
    return local(utc) if utc else "none"


def current_state(api):
    course = api.get(f"/courses/{COURSE_ID}")
    if not course:
        sys.exit(f"Cannot read course {COURSE_ID}")
    return dict(
        course=course,
        late_policy=(api.get(f"/courses/{COURSE_ID}/late_policy") or {}).get("late_policy"),
        groups={g["name"]: g for g in api.get_all(f"/courses/{COURSE_ID}/assignment_groups")},
        assignments={a["name"]: a for a in api.get_all(f"/courses/{COURSE_ID}/assignments")},
        modules={m["name"]: m for m in api.get_all(f"/courses/{COURSE_ID}/modules")},
    )


def print_plan(items, state):
    c = state["course"]
    print(f"Course {COURSE_ID}: {c['name']} ({c['workflow_state']}), time zone {c.get('time_zone')}")
    print(f"  apply_assignment_group_weights: {c.get('apply_assignment_group_weights')} (keep False, as in 36977)")
    print(f"  existing groups: {', '.join(state['groups']) or 'none'}")
    print(f"  existing assignments: {len(state['assignments'])}; existing modules: {len(state['modules'])}")
    print()

    print("LATE POLICY")
    lp = state["late_policy"]
    print(f"  now: {'none set' if not lp else json.dumps({k: lp.get(k) for k in LATE_POLICY})}")
    print(f"  plan: {'create' if not lp else 'update'} {json.dumps(LATE_POLICY)}")
    print(f"  No lock dates, as in MSB 341: the late policy handles late work. (lock_after is unused.) The most a")
    print("  late submission can lose is 90%, and nothing is accepted on day 10.")
    print()

    print("ASSIGNMENT GROUPS")
    for g in (MAIN_GROUP, EC_GROUP):
        print(f"  {g}: {'exists, reuse' if g in state['groups'] else 'create'}")
    print()

    print("ASSIGNMENTS (all grading_type=points, omit_from_final_grade=False, post_manually=True)")
    hdr = f"  {'#':>2}  {'Name':<48} {'Group':<13} {'Pts':>4}  {'Due (local)':<34} {'Lock (local)':<34} {'Submission':<18} {'Published':<9} Action"
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))
    for i, a in enumerate(items, 1):
        action = "exists, skip" if a["name"] in state["assignments"] else "create"
        print(f"  {i:>2}  {a['name']:<48} {a['group']:<13} {a['points_possible']:>4}  "
              f"{show_local(a['due_at']):<34} {show_local(a['lock_at']):<34} "
              f"{','.join(a['submission_types']):<18} {str(a['published']):<9} {action}")
    counted = sum(a["points_possible"] for a in items)
    print(f"\n  Points possible: {counted} (sprints {sum(a['points_possible'] for a in items if a['name'].startswith('Sprint'))}"
          f" + feedback 140). Extra credit assignments are 0 points possible, scored up to 10 each.")
    print("  The feedback placeholder stays unpublished, so Canvas shows the running total out of the")
    print("  published sprints until it is published in December.")
    print()

    print("MODULE")
    mod = "Sprints"
    print(f"  {mod}: {'exists, add missing items' if mod in state['modules'] else 'create'} (published)")
    print(f"    1. External URL: Sprints page -> {SPRINTS_PAGE} (opens in new tab)")
    k = 2
    for a in items:
        if a["in_module"]:
            print(f"    {k}. Assignment: {a['name']}")
            k += 1
    print()

    print("DESCRIPTIONS")
    for a in items:
        text = re.sub(r"<[^>]+>", "", a["description"])
        text = re.sub(r"\s+", " ", text).strip()
        print(f"  [{a['name']}]\n    {text}\n")
    bad = [a["name"] for a in items if "—" in a["description"]]
    if bad:
        sys.exit(f"em dash in description: {bad}")


def apply(api, items, state):
    lp = state["late_policy"]
    if lp:
        api.write("PATCH", f"/courses/{COURSE_ID}/late_policy", {"late_policy": LATE_POLICY})
        print("late policy updated")
    else:
        api.write("POST", f"/courses/{COURSE_ID}/late_policy", {"late_policy": LATE_POLICY})
        print("late policy created")

    groups = dict(state["groups"])
    for g in (MAIN_GROUP, EC_GROUP):
        if g not in groups:
            groups[g] = api.write("POST", f"/courses/{COURSE_ID}/assignment_groups", {"name": g})
            print(f"group created: {g}")

    created = dict(state["assignments"])
    for a in items:
        if a["name"] in created:
            print(f"exists, skipped: {a['name']}")
            continue
        body = {k: a[k] for k in ("name", "points_possible", "due_at", "lock_at", "submission_types",
                                  "published", "description", "grading_type",
                                  "omit_from_final_grade", "post_manually")}
        body["assignment_group_id"] = groups[a["group"]]["id"]
        created[a["name"]] = api.write("POST", f"/courses/{COURSE_ID}/assignments", {"assignment": body})
        print(f"created: {a['name']}")

    # The REST field post_manually is ignored on create (found 2026-10-22: every assignment came
    # back False and the first extra-credit scores posted). The post policy is GraphQL only.
    api.graphql(f'mutation {{ setCoursePostPolicy(input:{{courseId:"{COURSE_ID}", postManually:true}}) {{ errors {{ message }} }} }}')
    for a in items:
        aid = created[a["name"]]["id"]
        api.graphql(f'mutation {{ setAssignmentPostPolicy(input:{{assignmentId:"{aid}", postManually:true}}) {{ errors {{ message }} }} }}')
    print("post policy: manual, course and every assignment")

    mod = state["modules"].get("Sprints")
    if not mod:
        mod = api.write("POST", f"/courses/{COURSE_ID}/modules", {"module": {"name": "Sprints"}})
        print("module created: Sprints")
    existing = api.get_all(f"/courses/{COURSE_ID}/modules/{mod['id']}/items")
    have_urls = {i.get("external_url") for i in existing}
    have_ids = {i.get("content_id") for i in existing}
    pos = 1
    if SPRINTS_PAGE not in have_urls:
        api.write("POST", f"/courses/{COURSE_ID}/modules/{mod['id']}/items", {"module_item": {
            "type": "ExternalUrl", "title": "Sprints page", "external_url": SPRINTS_PAGE,
            "new_tab": True, "position": pos}})
    for a in items:
        if not a["in_module"]:
            continue
        pos += 1
        aid = created[a["name"]]["id"]
        if aid not in have_ids:
            api.write("POST", f"/courses/{COURSE_ID}/modules/{mod['id']}/items", {"module_item": {
                "type": "Assignment", "content_id": aid, "position": pos}})
    api.write("PUT", f"/courses/{COURSE_ID}/modules/{mod['id']}", {"module": {"published": True}})
    print("module items in place and module published")

    print("\nREAD BACK (local time, America/Denver)")
    for a in items:
        got = api.get(f"/courses/{COURSE_ID}/assignments/{created[a['name']]['id']}")
        ok = got and got.get("due_at") == a["due_at"] and got.get("lock_at") == a["lock_at"] \
            and float(got.get("points_possible") or 0) == a["points_possible"]
        print(f"  {'OK  ' if ok else 'DIFF'} {a['name']:<48} due {show_local(got.get('due_at')):<34} "
              f"lock {show_local(got.get('lock_at')):<34} {got.get('points_possible')} pts, "
              f"published {got.get('published')}")
    lp = (api.get(f"/courses/{COURSE_ID}/late_policy") or {}).get("late_policy") or {}
    print(f"  late policy: {json.dumps({k: lp.get(k) for k in LATE_POLICY})}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", default=True, help="print the plan (default)")
    mode.add_argument("--apply", action="store_true", help="create in Canvas, then read back")
    args = ap.parse_args()

    api = Canvas(allow_writes=args.apply)
    items = build_plan()
    state = current_state(api)
    print(f"MODE: {'APPLY' if args.apply else 'DRY RUN (GET requests only; nothing is changed)'}\n")
    print_plan(items, state)
    if args.apply:
        apply(api, items, state)


if __name__ == "__main__":
    main()
