# Review Package

## Commit Summary
- 8c1d3f9 "feat: initialize skills registry generator"

## Diff
diff --git a/scripts/generate_index.py b/scripts/generate_index.py
new file mode 100644
index 0000000..f924b1f
--- /dev/null
+++ b/scripts/generate_index.py
@@ -0,0 +1,15 @@
+import os
+import json
+import yaml
+from pathlib import Path
+
+# Base directory for skills
+SKILLS_DIR = "C:/code/ai/BrainStorming/skills"
+
+def generate_index():
+    index = []
+    print("Starting registry generation...")
+    # Implementation logic will be added here in next task
+    print("Registry generation complete.")
+    with open("skills-index.json", "w", encoding='utf-8') as f:
+        json.dump(index, f, indent=2)
+
+if __name__ == "__main__":
+    generate_index()
