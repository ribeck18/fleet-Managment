import json


def save_to_file(data: dict, file_path: str) -> dict:
    with open(file_path, "w") as f:
        json.dump(f, data, indent=4)

    return data
