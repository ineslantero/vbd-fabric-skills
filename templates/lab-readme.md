# Lab {{lab.number}}: {{lab.title}}

## Objective

{% for o in lab.objectives %}- {{o}}
{% endfor %}

## Why this matters for {{customer.name}}

{% for w in lab.why_it_matters %}- {{w}}
{% endfor %}

## Microsoft Learn references

{% for ref in lab.refs %}- [{{ref.title}}]({{ref.url}})
{% endfor %}

## Prerequisites

- Access to **Microsoft Fabric**.
- A Fabric capacity or trial SKU (see the workshop plan for the minimum SKU).
- Permission to create items in a Fabric workspace.
- The CSV files in this repo:
{% for f in lab.data_files %}  - `data/{{f}}`
{% endfor %}
{% if lab.fetch_script %}

## Step 0: Download the sample data

Grab the workshop dataset before you start:

- **PowerShell:** `./data/{{lab.fetch_script}}.ps1`
- **Bash:** `./data/{{lab.fetch_script}}.sh`

Safe to re-run — the script skips the download if the zip is already there.
{% endif %}
{% if lab.data_setup_options %}

## Data setup options

This lab does not require earlier labs to be completed. Use one of these options:

### Option A: You already have the data loaded

Use this if your Lakehouse already has these tables:

{% for t in lab.expected_tables %}- `{{t}}`
{% endfor %}

### Option B: Start fresh

- Create a training workspace, or use an existing dev workspace.
- Create a Lakehouse named using your name, e.g. `{{customer.slug}}_lab{{lab.number}}_lh_name`.
- Upload the CSVs listed above to the Lakehouse **Files** area.
- Load them into Lakehouse tables with the names listed in Option A.
{% endif %}

## Sample data

{% for f in lab.data_files_detail %}### `{{f.name}}`

- {{f.description}}
- Fields: {% for c in f.columns %}`{{c}}`{{ ", " if not loop.last }}{% endfor %}.

{% endfor %}

## Lab steps

{% for step in lab.steps %}### Step {{step.n}}: {{step.title}}

{% for b in step.bullets %}- {{b}}
{% endfor %}
{% if step.code %}
```{{step.code.language}}
{{step.code.content}}
```
{% endif %}
{% if step.explanation %}
**Explanation:** {{step.explanation}}
{% endif %}
{% if step.checkpoint %}
**Checkpoint:** {{step.checkpoint}}
{% endif %}
{% if step.preview_warning %}
> ⚠️ **Preview feature** — {{step.preview_warning}} ([roadmap card]({{step.preview_link}}))
{% endif %}

{% endfor %}

## Troubleshooting

{% for t in lab.troubleshooting %}- **{{t.symptom}}** → {{t.fix}}
{% endfor %}

## What's next

{{lab.next}}

---

<sub>Verified against Microsoft Learn on {{freshness.last_verified}}. Fabric release pinned: {{freshness.fabric_release_pinned}}. Freshness report: [`../../.vbd/freshness-{{module.id}}.yaml`](../../.vbd/freshness-{{module.id}}.yaml)</sub>
