# Migration Pilot: Legacy DB migration

## Goal
Convert legacy on-prem table structure into RDS Postgres using `bank-agent-skills` to demonstrate regulatory-compliant migration.

## Scope
- Schema mapping (Legacy SQL -> Postgres).
- Migration tool configuration.
- Validation of data parity.

## Success Metrics
- Data parity rate.
- Downtime during migration.

## Compliance Requirements
- Data residency: Postgres region selection.
- Encryption: At-rest and in-transit (TLS).
