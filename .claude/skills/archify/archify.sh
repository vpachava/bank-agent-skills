#!/bin/bash
# Archify Script

if [ ! -f "design.json" ]; then
  echo "Error: design.json not found in $(pwd)"
  exit 1
fi

TEMPLATE_DIR="/c/code/ai/BrainStorming/skills/diagram-templates"
OUTPUT_DIR="diagrams"
mkdir -p "$OUTPUT_DIR"

# Generate basic diagram with metadata
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
# Assuming simple artifact_id generation
ARTIFACT_ID="ART-$(date +%s)"

echo "Processing design into diagrams..."
# Basic processing logic:
# For now, create a simple C4 context diagram from design.json (placeholder for real mapping logic)
cp "$TEMPLATE_DIR/c4-context.md" "$OUTPUT_DIR/system-context.md"

# Inject metadata
sed -i "s/{{ artifact_id }}/$ARTIFACT_ID/g" "$OUTPUT_DIR/system-context.md"
sed -i "s/{{ generated_by }}/archify-engine/g" "$OUTPUT_DIR/system-context.md"
sed -i "s/{{ timestamp }}/$TIMESTAMP/g" "$OUTPUT_DIR/system-context.md"
sed -i "s/{{ system_name }}/Parsed-System/g" "$OUTPUT_DIR/system-context.md"

echo "Diagram generated in $OUTPUT_DIR/system-context.md"
