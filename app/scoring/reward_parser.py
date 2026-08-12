import re


def extract_reward(title):
    patterns = [
        # $100, $1,000, $14,999.50
        r"\$([\d,]+(?:\.\d+)?)",

        # 20 RTC, 35 RTC
        r"([\d,]+(?:\.\d+)?)\s+(RTC)",

        # [50 MRG]
        r"\[([\d,]+(?:\.\d+)?)\s+(MRG)\]",

        # 14999$
        r"\[([\d,]+(?:\.\d+)?)\$",
    ]

    for pattern in patterns:
        match = re.search(pattern, title, re.IGNORECASE)

        if match:
            amount = match.group(1).replace(",", "")

            return {
                "amount": float(amount),
                "currency": (
                    match.group(2).upper()
                    if len(match.groups()) > 1
                    else "USD"
                ),
            }

    return {
        "amount": None,
        "currency": None,
    }