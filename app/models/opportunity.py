class Opportunity:
    def __init__(self, title, description, reward, url, source, skills=None):
        self.title = title
        self.description = description
        self.reward = reward
        self.url = url
        self.source = source
        self.skills = skills or []


    def __repr__(self):
        return(
            f"Opportunity("
            f"title={self.title!r},"
            f"reward={self.reward!r},"
            f"source={self.source!r}"
            f")"
        )