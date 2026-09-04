from .reasoning import ReasoningEngine
from .knowledge import KnowledgeEngine


class LogyBrain:
    """
    Logy-এর মূল Brain controller.
    """

    def __init__(self):
        self.reasoning = ReasoningEngine()
        self.knowledge = KnowledgeEngine()

    def think(self, message: str) -> str:
        """
        User-এর message process করে উত্তর তৈরি করে।
        """

        if not message or not message.strip():
            return "Sir, আপনি কিছু লিখেননি।"

        message = message.strip()

        # Basic command handling
        if message.lower() in ["hello", "hi", "hey"]:
            return "Hello Sir! আমি Logy। কী করতে পারি?"

        if "তুমি কে" in message.lower():
            return "আমি Logy — আপনার নিজের AI system।"

        # Knowledge check
        knowledge_answer = self.knowledge.search(message)

        if knowledge_answer:
            return knowledge_answer

        # Reasoning engine
        return self.reasoning.process(message)
