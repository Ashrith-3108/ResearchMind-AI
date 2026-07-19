import hashlib
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List
from uuid import uuid4

from app.services.logger_service import logger


# ==========================================================
# TIMESTAMP
# ==========================================================

def timestamp() -> str:
    """
    Returns current timestamp.

    Example:
    20260718_154530
    """
    return datetime.now().strftime("%Y%m%d_%H%M%S")


# ==========================================================
# UUID
# ==========================================================

def generate_id() -> str:
    """
    Generate unique ID.
    """
    return str(uuid4())


# ==========================================================
# FILE HASH
# ==========================================================

def file_hash(file_path: str) -> str:
    """
    Generate SHA256 hash of file.
    """

    sha = hashlib.sha256()

    with open(file_path, "rb") as file:

        while True:

            chunk = file.read(4096)

            if not chunk:
                break

            sha.update(chunk)

    return sha.hexdigest()


# ==========================================================
# TEXT HASH
# ==========================================================

def text_hash(text: str) -> str:
    """
    Generate SHA256 hash of text.
    """

    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()


# ==========================================================
# JSON SAVE
# ==========================================================

def save_json(
    data: Dict,
    file_path: str,
):

    Path(file_path).parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        file_path,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False,
        )

    logger.info(f"Saved JSON -> {file_path}")


# ==========================================================
# JSON LOAD
# ==========================================================

def load_json(
    file_path: str,
) -> Dict:

    with open(
        file_path,
        "r",
        encoding="utf-8",
    ) as file:

        return json.load(file)


# ==========================================================
# CREATE DIRECTORY
# ==========================================================

def ensure_directory(path: str):

    Path(path).mkdir(
        parents=True,
        exist_ok=True,
    )


# ==========================================================
# FILE EXISTS
# ==========================================================

def file_exists(
    path: str,
) -> bool:

    return Path(path).exists()


# ==========================================================
# LIST FILES
# ==========================================================

def list_files(
    folder: str,
    extension: str = "",
) -> List[str]:

    folder = Path(folder)

    if not folder.exists():
        return []

    if extension:

        return [
            str(file)
            for file in folder.glob(f"*{extension}")
        ]

    return [
        str(file)
        for file in folder.iterdir()
        if file.is_file()
    ]


# ==========================================================
# FILE SIZE
# ==========================================================

def file_size_mb(
    file_path: str,
) -> float:

    size = os.path.getsize(file_path)

    return round(
        size / (1024 * 1024),
        2,
    )


# ==========================================================
# CLEAN TEXT
# ==========================================================

def clean_text(
    text: str,
) -> str:

    if not text:
        return ""

    text = text.replace("\x00", "")

    text = text.replace("\t", " ")

    text = text.replace("\r", "\n")

    while "\n\n\n" in text:
        text = text.replace("\n\n\n", "\n\n")

    while "  " in text:
        text = text.replace("  ", " ")

    return text.strip()


# ==========================================================
# REMOVE EMPTY VALUES
# ==========================================================

def remove_empty(
    data: Dict,
) -> Dict:

    cleaned = {}

    for key, value in data.items():

        if value in (
            None,
            "",
            [],
            {},
        ):
            continue

        cleaned[key] = value

    return cleaned


# ==========================================================
# FLATTEN DICTIONARY
# ==========================================================

def flatten_dict(
    dictionary: Dict,
    parent_key: str = "",
    separator: str = ".",
):

    items = []

    for key, value in dictionary.items():

        new_key = (
            f"{parent_key}{separator}{key}"
            if parent_key
            else key
        )

        if isinstance(value, dict):

            items.extend(
                flatten_dict(
                    value,
                    new_key,
                    separator,
                ).items()
            )

        else:

            items.append(
                (
                    new_key,
                    value,
                )
            )

    return dict(items)


# ==========================================================
# PRETTY PRINT
# ==========================================================

def pretty_json(
    data: Any,
) -> str:

    return json.dumps(
        data,
        indent=4,
        ensure_ascii=False,
    )