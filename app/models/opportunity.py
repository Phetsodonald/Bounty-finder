class Opportunity:
    def __init__(self, title, description, reward, currency, url, source, skills=None, skill_match=0):
        self.title = title
        self.description = description
        self.reward = reward
        self.currency = currency
        self.url = url
        self.source = source
        self.skills = skills or []
        self.skill_match = skill_match




    def __repr__(self):
        return (
            f"Opportunity("
            f"title={self.title!r}, "
            f"reward={self.reward!r}, "
            f"currency={self.currency!r}, "
            f"source={self.source!r}, "
            f"skills={self.skills!r}, "
            f"skill_match={self.skill_match!r}"
            f")"
        )