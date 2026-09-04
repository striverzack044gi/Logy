import json
from pathlib import Path


class KnowledgeBase:

    def __init__(self, file_path=None):

        if file_path is None:
            file_path = Path("data") / "knowledge.json"

        self.file_path = Path(file_path)

        self.file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.initialize()

    def initialize(self):

        if not self.file_path.exists():

            self.file_path.write_text(
                json.dumps(
                    {},
                    ensure_ascii=False,
                    indent=2
                ),
                encoding="utf-8"
            )

    def load(self):

        try:

            return json.loads(
                self.file_path.read_text(
                    encoding="utf-8"
                )
            )

        except Exception:

            return {}

    def add(self, key, value):

        data = self.load()

        data[key] = value

        self.file_path.write_text(
            json.dumps(
                data,
                ensure_ascii=False,
                indent=2
            ),
            encoding="utf-8"
        )

    def get(self, key):

        data = self.load()

        return data.get(key)
