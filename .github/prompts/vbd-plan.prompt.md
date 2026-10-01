---
mode: agent
description: Fabric VBD planner — turn a scoping call transcript into a proposal, agenda, prereqs and workshop.yaml.
---

Load the skill definition from `skills/vbd-plan/SKILL.md` in this repo and follow it end-to-end.

Key rules:
- Ask the CSA where the transcript lives (paste / WorkIQ meeting / email thread) before doing anything.
- Show module scoring reasoning before writing files.
- Every claim must cite Microsoft Learn or the Fabric roadmap via `components/freshness`.
- Never push to GitHub without explicit CSA approval.
- Agenda uses bullets with one-sentence rationale per item.
- Map each module to explain, demonstrate, practise, check and debrief; include exact lab step ranges, observable learner evidence and time for setup/practice/cleanup.
- Distinguish demonstration, hands-on and offline routes, with feature-specific prerequisites and a standalone replay path.
- Ground procedures in current Microsoft Learn pages and relevant verified Microsoft blog context. The freshness component is a review workflow, not an implemented API or proof of tenant execution.
