import yaml
from addict import Dict


def get_yaml_dict(path: str) -> Dict:
    with open(path, "r") as f:
        config_dict = yaml.safe_load(f)
    config = Dict(config_dict)
    return config
