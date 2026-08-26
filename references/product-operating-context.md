# Product Operating Context

Before reconstructing product state, establish the frame of investigation.

## Required
- Business product / journey
- Investigation objective
- Environment
- Time scope
- Available evidence sources or discoverable tool access
- Correlation / identity model
- Operator authority

## Business product description

Prefer a specific customer journey:

```yaml
product:
  name: Digital Lending — Personal Loan Application
  description: >
    Customer selects an offer, submits an application, completes
    eligibility and credit decisioning, accepts terms, and receives
    disbursement into the destination account.
  primary_actor: Existing retail customer
  intended_outcome: >
    Eligible customer receives the correctly booked and disbursed loan
    exactly once and sees a final confirmed state.
```

## Investigation scope

State must be scoped.

Examples:
- product-level operability assessment
- current production health
- funnel degradation
- single customer/application reconstruction
- incident
- recovery determination
- safe-action determination

Always distinguish current vs historical, production vs non-production, and individual entity vs cohort vs whole product.
