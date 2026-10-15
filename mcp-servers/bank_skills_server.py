# bank_skills_server.py
import sys, json, importlib

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No skill name provided"}))
        sys.exit(1)
    skill = sys.argv[1]
    try:
        module = importlib.import_module(f"{skill}.run")
    except Exception as e:
        print(json.dumps({"error": f"Could not load skill {skill}: {e}"}))
        sys.exit(1)
    if hasattr(module, "run"):
        try:
            result = module.run()
            print(json.dumps({"skill": skill, "result": result}))
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.exit(1)
    else:
        print(json.dumps({"error": f"Skill {skill} has no run() entry point"}))
        sys.exit(1)

if __name__ == "__main__":
    main()
