import re

from app.scoring.skills import MY_SKILLS


REQUIREMENT_MARKERS = [
    "requirements",
    "required",
    "skills",
    "technologies",
    "tech stack",
    "experience with",
    "knowledge of",
    "must have",
    "should have",
    "use",
    "using",
    "implement with",
]


def find_required_skills(text):
    text = text.lower()

    required_skills = []

    for skill in MY_SKILLS:
        pattern = rf"\b{re.escape(skill)}\b"

        if re.search(pattern, text):
            required_skills.append(skill)

    return required_skills


def calculate_skill_match(required_skills):
    if not required_skills:
        return 0

    total = sum(
        MY_SKILLS[skill]
        for skill in required_skills
    )

    maximum = len(required_skills) * 10

    return round((total / maximum) * 100)