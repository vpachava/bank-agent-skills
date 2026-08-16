# Capability Map: Digital Wallet Integration (UAE/Aani)

## 1. Scope & Decomposition
*   **Decomposition Depth:** Business Area → Domain → Service Domain for Payments, KYC, and Account management.
*   **Selective Adoption:** Focus on `Retail Payments` and `Customer Identity` domains; keep remaining domains at Business Area level.

## 2. BIAN-Aligned Map (In-Scope)

| Business Area | Domain | Service Domain |
| :--- | :--- | :--- |
| **Retail Banking** | Payments | **Payment Execution** (Aani/IP Rail) |
| **Retail Banking** | Payments | **Payment Settlement** (Recon/Netting) |
| **Customer** | Customer Identity | **Customer Onboarding** (KYC/UAE Pass) |
| **Customer** | Customer Identity | **Customer Profile** (Wallet/Account Balance) |

## 3. Realization (System Map)
*   **Payment Execution:** [New Aani-Gateway] → [Legacy Core-Adapter]
*   **Customer Identity:** [UAE Pass API] → [Legacy Core-KYC]
*   **Customer Profile:** [Digital Wallet Service] → [Legacy Core-DB]

## 4. Heat-Map (Current State)

| Capability | Maturity | Duplication | Strategic Focus | Reg Exposure |
| :--- | :--- | :--- | :--- | :--- |
| Payment Execution | Low (New) | None | High | High (Aani/CBUAE) |
| Customer Onboarding| Medium | High (Legacy & New)| High | High (KYC/AML) |

## 5. Selective Adoption Notes
*   **Payments Area:** Decomposed to Service Domain (as it is the initiative core).
*   **Governance Area:** Left at Business Area (not in-scope).
