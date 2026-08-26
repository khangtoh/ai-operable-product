# Example — Digital Lending Journey

## User input

> Business product: Digital Lending — Personal Loan Application.
>
> Customer selects an eligible offer, completes application and credit checks, accepts terms, and should receive disbursement into the destination account.
>
> Investigation: approved applications are stuck on Processing in production during the last two hours. Discover the evidence sources you can access before asking me for more.

## Expected skill behavior

1. Establish product context and intended outcome.
2. Discover available tools/sources.
3. Build a Source Capability Map.
4. Identify correlation keys such as application ID, workflow ID, trace ID, transaction ID.
5. Reconstruct expected vs implemented vs actual state.
6. Find the authoritative source for booked/disbursed loan state.
7. Do not conclude failure merely from an API timeout.
8. Determine Recovery Path before proposing a retry.
9. Check Policy Boundary for duplicate disbursement risk.
10. Describe Safe Actions only if preconditions and verification are established.
11. Assess AI-OPERABLE DONE and expose unknowns.

## Example reconstructed state

```text
Application LA-82972

Expected outcome:
Approved loan booked and funds disbursed exactly once.

Journey:
Application       COMPLETE
Eligibility       PASSED
Credit decision   APPROVED
Agreement          ACCEPTED
Disbursement       PROCESSING

Workflow:
Disbursement workflow started.
Core posting call timed out.
Authoritative posting state UNKNOWN.

Recovery:
Reconciliation required before any retry.

Policy:
Duplicate financial posting must not occur.

Safe action:
Run disbursement reconciliation if the action, authority, and verification mechanism are confirmed.

Confidence:
Medium until authoritative ledger state is inspected.
```
