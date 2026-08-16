# ADR-0001: API Gateway Facade

We are planning to use a new API Gateway facade to manage T24 interfaces. This seems faster and easier to deploy than building complex Domain API mapping logic in the middleware directly, and it avoids the overhead of formal architecture board reviews for every interface change. We'll proceed with the gateway approach.

### Consequences
- It's fast to implement.
- We don't have to document the mapping logic extensively.
- We might need to revisit this later if it becomes too rigid.
