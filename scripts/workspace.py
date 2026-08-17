import os
import fnmatch
from pathlib import Path
from domain_models import Skill, Workflow

class Workspace:
    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir).resolve()

    def get_taxonomy_path(self) -> Path:
        return self.root_dir / "docs" / "architecture" / "BANKING_WORKFLOWS_TAXONOMY.md"

    def load_taxonomy(self) -> set[str]:
        taxonomy_file = self.get_taxonomy_path()
        if not taxonomy_file.exists():
            return set()

        content = taxonomy_file.read_text(encoding="utf-8")
        artifacts = set()
        for line in content.splitlines():
            line = line.strip()
            if line.startswith("- `") and line.endswith("`"):
                artifacts.add(line[3:-1])
        return artifacts

    def _should_ignore(self, path: Path) -> bool:
        parts = path.parts
        for part in parts:
            if part.startswith('.') or part in ("graphify-out", "__pycache__", "node_modules", "venv"):
                return True
        return False

    def list_skills(self) -> dict[str, Skill]:
        skills = {}
        for root, dirs, files in os.walk(self.root_dir):
            root_path = Path(root)
            # Prune directory search for speed/correctness
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ("graphify-out", "__pycache__", "node_modules", "venv", "workflows", "docs", "test_temp")]

            if "SKILL.md" in files:
                skill_path = root_path / "SKILL.md"
                try:
                    rel_path = root_path.relative_to(self.root_dir)
                    skill_id = rel_path.as_posix()
                    # Prevent representing root folder itself as skill_id if SKILL.md is at root
                    if skill_id == ".":
                        skill_id = ""
                except ValueError:
                    continue

                content = skill_path.read_text(encoding="utf-8")
                skills[skill_id] = Skill(content, path=f"{skill_id}/SKILL.md")
        return skills

    def get_skill(self, skill_id: str) -> Skill | None:
        skill_path = self.root_dir / skill_id / "SKILL.md"
        if not skill_path.exists():
            return None
        content = skill_path.read_text(encoding="utf-8")
        return Skill(content, path=f"{skill_id}/SKILL.md")

    def write_skill(self, skill_id: str, content: str):
        skill_path = self.root_dir / skill_id / "SKILL.md"
        skill_path.parent.mkdir(parents=True, exist_ok=True)
        skill_path.write_text(content, encoding="utf-8")

    def list_workflows(self) -> dict[str, Workflow]:
        workflows = {}
        workflows_dir = self.root_dir / "workflows"
        if not workflows_dir.exists():
            return workflows

        for item in workflows_dir.iterdir():
            if item.is_file() and item.suffix.lower() in (".yaml", ".yml"):
                content = item.read_text(encoding="utf-8")
                workflows[item.name] = Workflow(content, name=item.stem)
        return workflows

    def get_workflow(self, workflow_name: str) -> Workflow | None:
        workflows_dir = self.root_dir / "workflows"
        wf_path = workflows_dir / workflow_name
        if wf_path.exists():
            content = wf_path.read_text(encoding="utf-8")
            return Workflow(content, name=wf_path.stem)
        # Try appending suffix if not present
        for suffix in (".yaml", ".yml"):
            alt_path = workflows_dir / f"{workflow_name}{suffix}"
            if alt_path.exists():
                content = alt_path.read_text(encoding="utf-8")
                return Workflow(content, name=alt_path.stem)
        return None

    def write_workflow(self, workflow_name: str, content: str):
        workflows_dir = self.root_dir / "workflows"
        workflows_dir.mkdir(parents=True, exist_ok=True)
        wf_path = workflows_dir / workflow_name
        wf_path.write_text(content, encoding="utf-8")

    def search_skills(self, pattern: str) -> dict[str, Skill]:
        all_skills = self.list_skills()
        matched = {}
        for skill_id, skill in all_skills.items():
            if fnmatch.fnmatch(skill_id, pattern) or pattern in skill_id:
                matched[skill_id] = skill
        return matched

    def search_workflows(self, pattern: str) -> dict[str, Workflow]:
        all_workflows = self.list_workflows()
        matched = {}
        for wf_name, wf in all_workflows.items():
            if fnmatch.fnmatch(wf_name, pattern) or pattern in wf_name:
                matched[wf_name] = wf
        return matched
