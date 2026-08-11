import re


def extract_reward(title):
    patterns = [
        r"\$(\d+(?:\.\d+)?)",
        r"(\d+(?:\.\d+)?)\s+(RTC)",
        r"\[(\d+(?:\.\d+)?)\s+(MRG)\]",
    ]

    for pattern in patterns:
        match = re.search(pattern, title, re.IGNORECASE)

        if match:
            return {
                "amount": float(match.group(1)),
                "currency": match.group(2)
                if len(match.groups()) > 1
                else "USD",
            }

    return {
        "amount": None,
        "currency": None,
    }