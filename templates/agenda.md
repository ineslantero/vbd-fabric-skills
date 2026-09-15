# {{customer.name}} — Fabric VBD agenda

**Duration:** {{constraints.duration_days}} days · **Mode:** {{constraints.delivery_mode}}

{% for day in agenda.days %}
## Day {{day.n}} — {{day.theme}}

{% for slot in day.slots %}
- **{{slot.start}}–{{slot.end}} · {{slot.title}}** — {{slot.rationale}}
{% endfor %}
{% endfor %}

## Notes
- Bullet-first, one-sentence rationale per item.
- Times shown in {{customer.timezone}}.
- Breaks and lunch pre-scheduled; move as needed for onsite delivery.
