$files = Get-ChildItem -Recurse -Filter SKILL.md -Path C:/code/ai/BrainStorming/skills | Where-Object { $_.FullName -notmatch "\.claude\\" -and $_.FullName -notmatch "\.scratch\\" }
foreach ($file in $files) {
    if ($file.FullName -match "\.scratch\\") { continue }
    
    $content = Get-Content -Raw $file.FullName
    
    $path = $file.FullName
    
    $togafPhase = "Phase A"
    $togafArtifact = "Architecture Vision"
    $bianDomain = "Customer Account.Origination"
    
    if ($path -match "architecture") { $togafPhase = "Phase C"; $togafArtifact = "HLD"; $bianDomain = "Integration.API" }
    elseif ($path -match "cloud") { $togafPhase = "Phase D"; $togafArtifact = "Deployment Diagram"; $bianDomain = "Integration.API" }
    elseif ($path -match "devops") { $togafPhase = "Phase G"; $togafArtifact = "Compliance Checklist"; $bianDomain = "Security.Auth" }
    elseif ($path -match "discovery" -or $path -match "documentation" -or $path -match "greenfield" -or $path -match "wayfinder") { $togafPhase = "Phase A"; $togafArtifact = "Architecture Vision"; $bianDomain = "Customer Account.Origination" }
    elseif ($path -match "integration") { $togafPhase = "Phase C"; $togafArtifact = "HLD"; $bianDomain = "Integration.API" }
    elseif ($path -match "migration" -or $path -match "modernization") { $togafPhase = "Phase F"; $togafArtifact = "Migration Plan"; $bianDomain = "Integration.Migration" }
    elseif ($path -match "security") { $togafPhase = "Phase D"; $togafArtifact = "Security Baseline"; $bianDomain = "Security.Auth" }
    elseif ($path -match "governance") { $togafPhase = "Phase G"; $togafArtifact = "Compliance Checklist"; $bianDomain = "Security.Auth" }
    
    if ($content -match "togaf-phases:") { continue }
    
    $newFrontmatter = "togaf-phases: [$togafPhase]`ntogaf-artifacts: [$togafArtifact]`nbian-service-domains: [$bianDomain]"
    
    # Split using flexible newlines
    $parts = $content -split '\r?\n---\r?\n', 2
    if ($parts.Count -eq 2) {
        $header = $parts[0]
        $body = $parts[1]
        
        $newHeader = $header + "`n" + $newFrontmatter
        # Ensure we maintain the structure
        $newContent = $newHeader + "`n---`n" + $body
        Set-Content -Path $file.FullName -Value $newContent -Encoding utf8
    }
}
