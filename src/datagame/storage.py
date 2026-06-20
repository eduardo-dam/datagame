import json
from pathlib import Path


def save_json(data: list, file_path: Path) -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
