# Remediation list — {{customer.name}} {{workshop.title}}

**{{session.label}} · {{session.date}}**
**Status:** template — to be completed live during the session
**Owner of this document:** {{csa.name}} · issued within {{deliverable.turnaround}} of the session

---

## How to use this

This is the **primary deliverable** for any review-style VBD. The labs exist to make the entries in it specific.

Add a row whenever a module checkpoint surfaces something that should change. Do not wait until the wrap-up to reconstruct the list — by the final session the detail will have gone.

**Priority:**

| | Meaning |
|---|---|
| **P1** | Security or compliance exposure. Act immediately. |
| **P2** | Material risk or significant inefficiency. Act this quarter. |
| **P3** | Should be corrected. Act when convenient. |
| **P4** | Noted. Revisit at the next review. |

**Effort:** S = under a day · M = a few days · L = a week or more · XL = needs its own piece of work.

---

{% for module in modules if module.include %}
## {{module.order}} — {{module.title}}

| # | Finding | Current state | Target state | Priority | Effort | Owner | Due |
|---|---|---|---|---|---|---|---|
{% for n in range(1, 4) %}
| {{module.order}}.{{n}} | | | | | | | |
{% endfor %}

{% if module.prompts %}
**Prompts if the list is thin:**
{% for p in module.prompts %}
- {{p}}
{% endfor %}
{% endif %}

{% if module.focus_table %}
> ### ⚠️ {{module.focus_table.title}}
>
> {{module.focus_table.rationale}}
>
> | {{module.focus_table.columns | join(' | ')}} |
> |{% for c in module.focus_table.columns %}---|{% endfor %}
> |{% for c in module.focus_table.columns %} |{% endfor %}
> |{% for c in module.focus_table.columns %} |{% endfor %}
>
> {{module.focus_table.note}}
{% endif %}

{% if module.commitment %}
### {{module.commitment.title}}

{{module.commitment.rationale}}

| | |
|---|---|
{% for f in module.commitment.fields %}
| **{{f}}** | |
{% endfor %}
{% endif %}

---

{% endfor %}

## Carried forward — not this session's scope

Items that surfaced but belong to another session or engagement. Recorded so they are not lost.

{% for s in related_sessions if not s.current %}
### → {{s.title}}
{% if s.status %}*({{s.status}})*{% endif %}

| # | Item | Note |
|---|---|---|
| {{s.prefix}}.1 | | |
| {{s.prefix}}.2 | | |

{% if s.deadline_note %}
> {{s.deadline_note}}
{% endif %}

{% endfor %}

---

## Summary

_Complete during the wrap-up._

| Priority | Count | Owners assigned |
|---|---|---|
| P1 | | |
| P2 | | |
| P3 | | |
| P4 | | |

**The three things to do first:**

1.
2.
3.

**Agreed review point:** _______________

---

## Attendance

| Name | Role | Organisation | Modules attended |
|---|---|---|---|
| | | | |

---

<sub>{{customer.name}} {{workshop.title}} · Prepared by {{csa.name}}, {{csa.title}} · Content verified against Microsoft Learn on {{freshness.last_verified}}, Fabric release pinned {{freshness.fabric_release_pinned}}.</sub>
