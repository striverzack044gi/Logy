from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

MEMORY_FILE = DATA_DIR / "memory.json"

KNOWLEDGE_FILE = DATA_DIR / "knowledge.json"

HOST = "127.0.0.1"

PORT = 5000

DEBUG = False
