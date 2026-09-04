class KnowledgeEngine:
    """
    Logy-এর internal knowledge layer.

    ভবিষ্যতে এখানে নিজের knowledge base,
    documents এবং learned information যুক্ত করা যাবে।
    """

    def __init__(self):
        self.knowledge = {
            "logy": "Logy হলো একটি personal AI system.",
            "python": "Python একটি general-purpose programming language.",
            "github": "GitHub source code এবং project version control-এর জন্য ব্যবহৃত হয়.",
        }

    def search(self, query: str):

        query_lower = query.lower()

        for key, value in self.knowledge.items():

            if key in query_lower:
                return value

        return None
