from app.scoring.skill_matcher import calculate_skill_match, find_required_skills

def test_find_required_skills():
    text = """
    Build a Django REST API with PostgreSQL.
    """

    skills = find_required_skills(text)

    assert "django" in skills
    assert "api" in skills
    assert "sql" in skills


def test_calculate_skill_match():
    skills = [
        "django",
        "api",
        "sql",
    ]

    score = calculate_skill_match(skills)

    assert score == 66