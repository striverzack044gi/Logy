from pathlib import Path


def read_text_file(file_path):

    path = Path(file_path)

    if not path.exists():
        return None

    if not path.is_file():
        return None

    try:

        return path.read_text(
            encoding="utf-8"
        )

    except UnicodeDecodeError:

        return path.read_text(
            encoding="utf-8",
            errors="ignore"
        )
