from pathlib import Path
import yaml

params = {}

def flatten_yaml(cfg_dict):
    result = {}
    for k, v in cfg_dict.items():
        if isinstance(v, dict):
            result = result | v
        else:
            result[k] = v
    return result


def load_default():
    global params
    default_path = Path(__file__).parent / "cfg" / "default.yaml"
    with open(default_path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)
    params = flatten_yaml(raw)

    for k, v in params.items():
        globals()[k] = v


def update_from_yaml(yaml_path):
    if yaml_path is None:
        return

    global params

    yaml_path = Path(yaml_path)
    with open(yaml_path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    new_vals = flatten_yaml(raw)
    params = {**params, **new_vals}

    for k, v in params.items():
        globals()[k] = v


load_default()

