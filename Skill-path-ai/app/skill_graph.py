import json
import os

DATA_FOLDER = "data"

FILES = [
    "programming_domain.json",
    "dsa_domain.json",
    "web_domain.json",
    "data_ai_domain.json",
    "systems_devops_domain.json",
    "security_domain.json"
]


def load_skill_graph():
    skill_graph = {}

    for file in FILES:
        path = os.path.join(DATA_FOLDER, file)

        with open(path, "r") as f:
            data = json.load(f)

            for skill, details in data.items():
                skill_graph[skill] = details

    return skill_graph