# Evidence Fabric and Source Capability Map

A connected source is valuable only when the agent understands **what it can establish**.

## Source Capability Map

For each source capture:

```yaml
name:
type:
can_establish: []
freshness:
identifiers: []
authority_for: []
limitations: []
access_mode: read | action
```

## Typical evidence roles

### Product specifications
Good for expected outcome and intended journey.

### Source repositories
Good for implemented behavior, API contracts, state transitions, identifiers, and error handling. Deployment state must be validated.

### Observability
Good for runtime execution, failures, latency, traces, and technical symptoms.

### Business analytics
Good for user journey and business-event outcomes when instrumentation is trustworthy.

### Workflow engines
Good for workflow execution, state, retry, and pending work.

### Core/ledger/system of record
Potentially authoritative for booked business state.

### Incident and ticket systems
Good for known failure patterns, changes, defects, and historical context.

### Runbooks
Good for intended recovery procedures, but freshness and test status matter.

### Policy/IAM
Good for operational constraints and action authority.

### Support systems
Good for customer-visible symptoms and recurring supportability gaps.

## Important rule

Do not infer product success from infrastructure signals when an authoritative business-state source exists or is required.
