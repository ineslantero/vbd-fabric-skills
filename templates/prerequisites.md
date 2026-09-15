# {{customer.name}} — Workshop prerequisites

**Please complete by {{prereq_deadline}}.** Missing prereqs will cost workshop time — items marked ⚠️ are blockers.

## 1. Fabric tenant & capacity ⚠️
- **Capacity SKU:** {{prerequisites.capacity}} minimum, running in {{constraints.regions | join}}.
- **Tenant settings** (Fabric admin portal → Tenant settings):
{% for s in prerequisites.tenant_settings %}
  - {{s}}
{% endfor %}
- Reference: [Enable Microsoft Fabric for your organization](https://learn.microsoft.com/fabric/admin/fabric-switch)

## 2. Licences ⚠️
{% for l in prerequisites.licences %}
- {{l}}
{% endfor %}

## 3. Attendee setup
{% for a in prerequisites.attendee_setup %}
- {{a}}
{% endfor %}

## 4. Data
{{prerequisites.data_upload}}

## 5. Access checklist (per attendee)
- [ ] Signed in to `app.fabric.microsoft.com`
- [ ] Can see the workshop workspace
- [ ] Can create a Lakehouse (verifies capacity + tenant settings)
- [ ] Power BI Pro / PPU licence assigned

## Troubleshooting
- Can't create Fabric items → check tenant setting `Users can create Fabric items` and capacity assignment.
- No capacity visible → confirm F-SKU is running and workspace is assigned to it.
- SSO issues → confirm attendees are in the customer's home tenant, not a guest tenant.
