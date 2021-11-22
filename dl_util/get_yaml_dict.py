"""
Copyright (c) 2021 Mana Masuda
This software is released under the MIT License, see LICENSE.
"""

import yaml
from addict import Dict


def get_yaml_dict(path: str) -> Dict:
    with open(path, "r") as f:
        config_dict = yaml.safe_load(f)
    config = Dict(config_dict)
    return config
