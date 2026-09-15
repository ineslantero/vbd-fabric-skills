# {{customer.name}} — Microsoft Fabric Value-Based Delivery proposal

**Prepared by:** {{csa.name}}
**Date:** {{today}}
**Duration:** {{constraints.duration_days}} days ({{constraints.delivery_mode}})
**Attendees:** {{customer.audience_size}} ({{customer.persona_mix | join}})
**Fabric release pinned:** {{freshness.fabric_release_pinned}}

## Customer context

- **Industry:** {{customer.industry}}
- **Current stack:** {{constraints.existing_stack | join}}
- **Sensitivity:** {{customer.sensitivity}}

## Objectives (from scoping call)

{% for obj in objectives %}
- {{obj}}
{% endfor %}

## Recommended modules

{% for m in modules %}
{% if m.include %}
- **{{m.id | title}}** — {{m.duration_hours}}h. {{m.customer_angle}}
{% endif %}
{% endfor %}

### Modules deliberately excluded
{% for m in modules %}
{% if not m.include %}
- **{{m.id | title}}** — {{m.reason}}
{% endif %}
{% endfor %}

## Data strategy

{{data_strategy.mode | title}} — domain: **{{data_strategy.domain}}**. Volumes and schema documented in `data/README.md`.

## Future capabilities to watch

_Populated from the Fabric roadmap by `components/freshness` at generation time. Each item links to the roadmap card._

## Next steps

- CSA and customer review this proposal and `agenda.md`.
- Customer completes `prerequisites.md` before Day -3.
- Lab repo delivered Day -1 for offline review.

## References

_Generated citation list — every claim in this proposal links to Microsoft Learn or the Fabric roadmap._
