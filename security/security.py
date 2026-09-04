import hashlib


class Security:

    @staticmethod
    def hash_text(text: str):

        return hashlib.sha256(
            text.encode("utf-8")
        ).hexdigest()

    @staticmethod
    def verify_text(text: str, hashed: str):

        return (
            Security.hash_text(text)
            == hashed
        )
