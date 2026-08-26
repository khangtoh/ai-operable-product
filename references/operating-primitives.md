# Seven Operating Primitives

## 1. Outcome Intent
**Question:** What does success mean?

Defines the customer/business outcome the product should produce. System health is not automatically product success.

## 2. Journey Context
**Question:** Where is the user?

Provides enough business and interaction context to reconstruct what the user was trying to do, what they experienced, and where they are/were in the journey.

## 3. Workflow Map
**Question:** How does work move?

Describes how work progresses toward the outcome across services, APIs, events, workflows, databases, external dependencies, and human handoffs.

## 4. Recovery Path
**Question:** How does failure resolve?

Defines designed mechanisms such as retry, compensation, reconciliation, rollback, replay, repair, failover, refund, or escalation.

## 5. Policy Boundary
**Question:** What must not happen?

Defines constraints, authorization, approvals, regulatory controls, privacy requirements, blast-radius limits, and prohibited actions.

## 6. Safe Actions
**Question:** What can be done?

Defines operational actions with explicit preconditions, authority, scope, bounded consequences, verification, auditability, and rollback/reversibility where relevant.

## 7. Feedback Loop
**Question:** How does the product learn?

Defines how production evidence changes future code, tests, runbooks, policies, automation, agent instructions, architecture, product design, or customer journey.

## Principle

A product that cannot express these primitives cannot be reliably reasoned about by an AI operator.
