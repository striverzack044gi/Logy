from memory.memory import Memory


def test_memory(tmp_path):

    memory_file = tmp_path / "memory.json"

    memory = Memory(memory_file)

    memory.add(
        "Hello",
        "Hi Sir!"
    )

    data = memory.load()

    assert len(data) == 1
    assert data[0]["user"] == "Hello"
