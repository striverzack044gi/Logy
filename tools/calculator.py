def calculate(expression: str):

    """
    Basic calculator.

    শুধুমাত্র mathematical characters allow করা হয়েছে।
    """

    allowed = set(
        "0123456789+-*/().% "
    )

    if not expression:
        return None

    if any(char not in allowed for char in expression):
        return None

    try:
        return eval(
            expression,
            {"__builtins__": {}},
            {}
        )

    except Exception:
        return None
