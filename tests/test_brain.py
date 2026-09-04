from brain.brain import LogyBrain


def test_brain():

    brain = LogyBrain()

    response = brain.think("Hello")

    assert response
