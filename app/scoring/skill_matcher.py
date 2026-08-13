from app.scoring.skills import MY_SKILLS

def find_required_skills(text):
    text = text.lower()

    found = []

    for skill in MY_SKILLS:
        if skill in  text:
            found.append(skill)

    return found

def calculate_skill_match(required_skills):
    if not required_skills:
        return 0

    total = 0

    for skill in required_skills:
        total += MY_SKILLS[skill]

    maximum = len(required_skills) * 10

    return round((total / maximum) * 100)