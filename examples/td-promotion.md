# Example — Term Deposit Promotion Journey

## Product summary

Existing eligible customers receive a promotional term-deposit offer, select amount and tenor, fund it from a source account, and should receive a correctly created TD carrying the promotional rate.

## Intended outcome

An eligible customer successfully opens the promotional TD with correct funding amount, correct tenor, correct promotional rate, exactly one funding debit, exactly one TD account, and customer confirmation.

## Expected business journey

```text
Eligibility
→ Offer Display
→ Offer Selection
→ Funding Account Selection
→ Confirmation
→ Debit Source Account
→ Create TD
→ Apply Promotional Rate
→ Customer Confirmation
```

## Useful evidence

Product/offer specification, feature flag or eligibility configuration, journey analytics, source-account debit transaction, TD account creation state, promotional-rate configuration, workflow execution, runtime traces/logs, reconciliation procedure, duplicate-debit/account policy, support cases, and incident history.

## Critical reasoning rule

HTTP 200 from the enrollment API does not prove the TD was successfully funded, created, and assigned the promotional rate. Product outcome requires authoritative business-state evidence.
