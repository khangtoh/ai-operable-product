# Product State

Product State is an evidence-backed operational representation of a business journey at a specific scope and time.

It is not a dashboard or a log summary.

## Three-state comparison

### Expected
What should happen according to business/product intent.

### Implemented
What code, configuration, workflow definitions, and current architecture implement.

### Actual
What runtime and business-state evidence says happened.

## Example

```yaml
product_state:
  product: Digital Lending — Personal Loan Application
  entity: LA-82972
  as_of: 2026-08-26T10:43:00+08:00

  intended_outcome:
    expected: Loan booked and funds disbursed exactly once
    observed: Pending
    status: not_yet_confirmed

  journey:
    completed:
      - application
      - eligibility
      - credit_decision
      - agreement
    current: disbursement
    customer_visible_state: Processing

  workflow:
    disbursement: started
    core_posting: unknown
    notification: not_started

  runtime:
    - core API timeout at 10:42:18

  recovery:
    required: reconciliation

  policy:
    - Do not retry until ledger state is known

  safe_actions:
    - action: run_disbursement_reconciliation
      precondition: application_id known
      verification: authoritative ledger lookup

  confidence:
    overall: medium
    unknowns:
      - authoritative ledger posting state
```
