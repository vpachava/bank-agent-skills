---
name: retail-architecture
owner: Retail & E-Commerce Architecture
version: 0.1.0
description: "Use when designing PCI-DSS v4.0 enhanced, SOC 2 Type II, and high-throughput retail e-commerce architectures."
expected-deliverables:
  - PCI-DSS v4.0 CDE (Cardholder Data Environment) Boundary Map
  - SOC 2 Type II Continuous Audit Architecture
togaf-phases: [Phase C, Phase D]
---

# /industries/retail

## Overview
Architectural guardrails for high-volume retail platforms, payment gateways, and e-commerce systems. Enforces strict PCI-DSS v4.0 Cardholder Data Environment (CDE) segmentation, tokenization, and SOC 2 Type II audit readiness.

## Process
1. **CDE Boundary Isolation:** Decouple cardholder data capture from general e-commerce web applications using merchant vault tokenization.
2. **Script Integrity (PCI-DSS v4.0 Req 6.4.3):** Monitor and manage all payment-page scripts to prevent Magecart/form-jacking attacks.
3. **High-Availability Scaling:** Design auto-scaling storefronts capable of handling flash-sale throughput (Black Friday/Cyber Monday).
