from governance_engine import GovernanceEngine

def generate_dashboard():
    engine = GovernanceEngine()
    return engine.execute_unified_audit()

if __name__ == "__main__":
    import json
    print(json.dumps(generate_dashboard(), indent=2))
