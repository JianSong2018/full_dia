from pathlib import Path
import yaml

CONFIG_PATH = Path(__file__).parent/'cfg'/'default.yaml'

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    cfg = yaml.safe_load(f)

params = {}
for k, v in cfg.items():
    if not isinstance(v, dict): # remove the first header
        params[k] = v
    else:
        params = params | v

for k, v in params.items():
    globals()[k] = v

