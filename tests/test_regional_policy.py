import yaml
from pathlib import Path

def test_regional_policy_files():
    policy_dir = Path(__file__).parents[1] / "governance" / "policy" / "regional"
    
    assert policy_dir.exists()
    
    uae_policy = policy_dir / "uae_cbuae.yaml"
    ksa_policy = policy_dir / "ksa_sama.yaml"
    eu_policy = policy_dir / "eu_dora.yaml"
    
    assert uae_policy.exists()
    assert ksa_policy.exists()
    assert eu_policy.exists()
    
    with open(uae_policy, 'r') as f:
        data = yaml.safe_load(f)
        assert data["region"] == "UAE"
        assert len(data["regulations"]) >= 2
        
    with open(ksa_policy, 'r') as f:
        data = yaml.safe_load(f)
        assert data["region"] == "KSA"
        
    with open(eu_policy, 'r') as f:
        data = yaml.safe_load(f)
        assert data["region"] == "EU"
