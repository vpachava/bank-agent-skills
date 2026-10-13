from governance_engine import GovernanceEngine

if __name__ == "__main__":
    import sys
    engine = GovernanceEngine()
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    print(engine.run_staleness_check(days))
