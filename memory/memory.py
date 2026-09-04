import json
from pathlib import Path


class Memory:
    """
    Logy-এর local memory system.

    Memory file শুধুমাত্র local device storage-এ থাকবে।
    GitHub-এ runtime memory রাখা হবে না।
    """

    def __init__(self, file_path=None):

        if file_path is None:
            file_path = Path("data") / "memory.json"

        self.file_path = Path(file_path)

        self.file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self._initialize()

    def _initialize(self):

        if not self.file_path.exists():

            self.file_path.write_text(
                json.dumps(
                    [],
                    ensure_ascii=False,
                    indent=2
                ),
                encoding="utf-8"
            )

    def load(self):

        try:

            data = json.loads(
                self.file_path.read_text(
                    encoding="utf-8"
                )
            )

            if isinstance(data, list):
                return data

        except Exception:
            pass

        return []

    def save(self, memories):

        self.file_path.write_text(
            json.dumps(
                memories,
                ensure_ascii=False,
                indent=2
            ),
            encoding="utf-8"
        )

    def add(self, user_message, logy_response):

        memories = self.load()

        memories.append({
            "user": user_message,
            "logy": logy_response
        })

        self.save(memories)

    def get_recent(self, limit=10):

        memories = self.load()

        return memories[-limit:]

    def clear(self):

        self.save([])
