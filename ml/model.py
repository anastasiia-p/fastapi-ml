from pathlib import Path

import yaml
from transformers import pipeline

config_path = Path(__file__).parent / "config.yaml"
with open(config_path, "r") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)


def load_model():
    return pipeline(config["task"], model=config["model"], device=-1)
