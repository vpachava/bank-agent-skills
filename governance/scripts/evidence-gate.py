from governance_engine import GovernanceEngine

if __name__ == "__main__":
    import sys
    engine = GovernanceEngine()
    if len(sys.argv) > 1:
        res = engine.run_evidence_gate(sys.argv[1])
        print(res)
    else:
        print(engine.run_evidence_gate())
