$file = 'C:/code/ai/BrainStorming/skills/architecture/c4-model/SKILL.md'
$content = Get-Content -Raw $file
# Check the actual line endings.
# It might be \r\n
$parts = $content -split '\r?\n---\r?\n', 2
Write-Host "Parts count: $($parts.Count)"
