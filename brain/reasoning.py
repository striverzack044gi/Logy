class ReasoningEngine:
    """
    Logy-এর reasoning layer.

    ভবিষ্যতে এখানে:
    - Planning
    - Decision making
    - Context analysis
    - Multi-step reasoning
    - Tool selection
    ইত্যাদি যোগ করা হবে।
    """

    def process(self, message: str) -> str:

        message_lower = message.lower()

        if "ধন্যবাদ" in message_lower:
            return "স্বাগতম Sir! 😊"

        if "কেমন আছো" in message_lower:
            return "আমি ভালো আছি Sir। আপনার command-এর অপেক্ষায় আছি।"

        return (
            f"Sir, আমি আপনার কথাটি বুঝেছি:\n\n"
            f"“{message}”\n\n"
            "এখন আমার reasoning system আরও উন্নত করা হবে।"
        )
