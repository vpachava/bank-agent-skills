$report = "# TOGAF and BIAN Coverage Mapping Report`n`n"
$report += "| Skill | TOGAF Phase | TOGAF Artifact | BIAN Service Domain |`n"
$report += "|-------|-------------|----------------|---------------------|`n"

$files = Get-ChildItem -Recurse -Filter SKILL.md -Path C:/code/ai/BrainStorming/skills | Where-Object { $_.FullName -notmatch "\.claude\\" -and $_.FullName -notmatch "\.scratch\\" }

foreach ($file in $files) {
    if ($file.FullName -match "\.scratch\\") { continue }
    
    $content = Get-Content -Raw $file.FullName
    if ($content -match "togaf-phases: \[(.*?)\]") {
        $phase = $matches[1]
        
        $artifact = "N/A"
        if ($content -match "togaf-artifacts: \[(.*?)\]") { $artifact = $matches[1] }
        
        $bian = "N/A"
        if ($content -match "bian-service-domains: \[(.*?)\]") { $bian = $matches[1] }
        
        $name = $file.Directory.Name
        $report += "| $name | $phase | $artifact | $bian |`n"
    }
}
$report | Out-File -FilePath TOGAF-BIAN-Coverage.md -Encoding utf8
