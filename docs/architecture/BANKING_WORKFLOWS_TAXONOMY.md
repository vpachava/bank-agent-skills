# Banking Workflow Composition Taxonomy

## Artifact Types (I/O Contracts)
- `Requirements_Baseline`
- `Architecture_Vision`
- `HLD`
- `LLD`
- `Security_Compliance_Pack`
- `Deployment_Diagram`
- `Migration_Plan`
- `Data_Mapping_Schema`
- `API_Contract`

## Workflow Schema (YAML)
```yaml
name: <Pattern Name>
description: <Brief description>
sequence:
  - skill_id: <folder/path/to/skill>
    inputs: [<list of Artifact Types>]
    outputs: [<list of Artifact Types>]
```
