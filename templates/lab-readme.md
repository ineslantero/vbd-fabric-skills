# Lab {{lab.number}}: {{lab.title}}

> **Module:** {{module.id | title}} · **Duration:** ~{{lab.duration_minutes}} min · **Personas:** {{lab.personas | join}}
>
> _Content verified against Microsoft Learn on {{freshness.last_verified}}. Fabric release pinned: {{freshness.fabric_release_pinned}}._

## Learning objectives

By the end of this lab you will be able to:
{% for o in lab.objectives %}
- {{o}}
{% endfor %}

## Customer context

{{lab.customer_angle}}

## Prerequisites

- Completed [`prerequisites.md`](../../prerequisites.md).
- Access to workspace **{{customer.workspace_name}}**.
- Sample data loaded (see [`../../data/README.md`](../../data/README.md)).

## Steps

{% for step in lab.steps %}
### Step {{step.n}}: {{step.title}}

{{step.body}}

{% if step.checkpoint %}
✅ **Checkpoint** — {{step.checkpoint}}
{% endif %}

{% if step.preview_warning %}
⚠️ **Preview feature** — {{step.preview_warning}} ([roadmap card]({{step.preview_link}}))
{% endif %}

_References:_
{% for ref in step.refs %}
- [{{ref.title}}]({{ref.url}})
{% endfor %}
{% endfor %}

## Troubleshooting

{% for t in lab.troubleshooting %}
- **{{t.symptom}}** → {{t.fix}}
{% endfor %}

## What's next

{{lab.next}}

---

<sub>Freshness report: [`../../.vbd/freshness-{{module.id}}.yaml`](../../.vbd/freshness-{{module.id}}.yaml)</sub>
