# Lab {{lab.number}}: {{lab.title}}

## Outcome and learning route

{% for o in lab.objectives %}- {{o}}
{% endfor %}

**Route:** {{lab.learning_mode}}. **Time:** {{lab.duration_minutes}} minutes, including setup, learner practice, validation and cleanup.
**You will create:** {{lab.output_artifact}}.
**Starting point:** {{lab.starting_state}}.

Observation and offline design exercises are useful alternatives, but do not count as executing this lab in Fabric. Record the route you actually completed.

## Why this matters for {{customer.name}}

{% for w in lab.why_it_matters %}- {{w}}
{% endfor %}

## Before you start

- Workspace and learner-specific item prefix: {{lab.item_prefix}}. Replace labelled placeholders before running code.
- Required workspace/item roles: {{lab.required_roles}}.
- Feature-specific capacity, licence, region and tenant settings: {{lab.feature_prerequisites}}. A trial is not a universal substitute for paid capacity.
- Setup owner and readiness check: {{lab.setup_owner}}; {{lab.readiness_check}}.
- Cost and change boundary: {{lab.safety_boundary}}. Use synthetic data and an approved training environment; do not change tenant-wide settings, share externally or send notifications just to complete an exercise.
- Blocked-feature alternative: {{lab.fallback}}. Label evidence as observed or offline, not executed.

## Data and dependencies

{% for f in lab.data_files %}- Repository input: `data/{{f}}`.
{% endfor %}

{% for f in lab.data_files_detail %}### `{{f.name}}`

{{f.description}}

Fields: {% for c in f.columns %}`{{c}}`{{ ", " if not loop.last }}{% endfor %}.
Expected input rows and types: {{f.validation}}.

{% endfor %}

{% if lab.fetch_script %}Run the documented platform-specific script from the repository root:

- PowerShell: `& .\data\{{lab.fetch_script}}.ps1`
- Bash: `bash ./data/{{lab.fetch_script}}.sh`

Check the script's documented destination, integrity check and rerun behaviour before using downloaded data.
{% endif %}

{% if lab.data_setup_options %}This lab supports two starting routes:

- **Reuse:** verify these existing tables and their schemas before skipping ingestion:
{% for t in lab.expected_tables %}  - `{{t}}`
{% endfor %}
- **Start fresh:** {{lab.standalone_setup}}. Link to exact numbered ingestion steps or include the complete upload/load procedure; "load the data" alone is not a procedure.
{% endif %}

## How to do it

{% for step in lab.steps %}### Step {{step.n}}: {{step.title}}

**Run as:** {{step.persona}}. **Where:** {{step.surface}}. **Time:** {{step.minutes}} minutes.

{% for b in step.bullets %}{{loop.index}}. {{b}}
{% endfor %}
{% if step.code %}
```{{step.code.language}}
{{step.code.content}}
```

**Run instructions:** {{step.code.run_instructions}}
{% endif %}

**Expected result:** {{step.expected_result}}

**Checkpoint:** {{step.checkpoint}}

**If it fails:** {{step.recovery}}

**Why:** {{step.explanation}}

**Procedure source:** [{{step.source.title}}]({{step.source.url}}), checked {{step.source.checked_on}}. Cite the relevant section and distinguish documentation review from tenant execution.
{% if step.preview_warning %}
> **Preview or availability constraint:** {{step.preview_warning}} ([status source]({{step.preview_link}})). Do not assume roadmap availability means your tenant has the feature.
{% endif %}

{% endfor %}

## Your turn

**Change:** {{lab.challenge.task}}

**Predict before running:** {{lab.challenge.prediction}}

**Evidence to capture:** {{lab.challenge.evidence}}

**Success criteria:** {{lab.challenge.success_criteria}}

**Hint:** {{lab.challenge.hint}}

## Troubleshooting

{% for t in lab.troubleshooting %}- **{{t.symptom}}**: {{t.fix}}
{% endfor %}

## Cleanup and rerun

{% for action in lab.cleanup %}{{loop.index}}. {{action}}
{% endfor %}

**Rerun behaviour:** {{lab.rerun_behaviour}}. Remove only items created for this exercise; never delete a shared workspace, production tables or a shared capacity.

## Completion evidence

| Check | Evidence |
|---|---|
| Artifact created and inspected | {{lab.completion.artifact}} |
| Result compared with expected output | {{lab.completion.result}} |
| Learner change completed | {{lab.completion.challenge}} |
| Cleanup / retained resources recorded | {{lab.completion.cleanup}} |
| Actual route | Executed / observed / offline / blocked |

Do not include tokens, connection strings, real personal data or unapproved tenant identifiers in screenshots, logs or commits.

## Sources and further reading

{% for ref in lab.refs %}- [{{ref.title}}]({{ref.url}}) - {{ref.role}}; checked {{ref.checked_on}}.
{% endfor %}

Microsoft Learn is the procedural authority. Microsoft blog posts supply dated examples and design context, not proof that a feature is enabled or generally available.

## What's next

{{lab.next}}

---

<sub>Documentation reviewed: {{freshness.last_verified}}. Release reference: {{freshness.fabric_release_pinned}} (not a runtime version lock). Execution evidence: {{lab.execution_status}}. Source and unresolved-issue record: [`../../FRESHNESS.md`](../../FRESHNESS.md).</sub>
