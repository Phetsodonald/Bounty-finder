import requests
from app.models.opportunity import Opportunity
from app.scoring.reward_parser import extract_reward

GITHU_API = "https://api.github.com/search/issues"

def find_opportunities():
    params = {
        "q": "label:bounty state:open",
        "sort": "updated",
        "order": "desc",
        "per_page": 20
    }

    response = requests.get(
        GITHU_API,
        params=params, 
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    opportunities = []

    for item in data.get("items", []):
        reward = extract_reward(item["title"])

        opportunity = Opportunity(
            title=item["title"],
            description=item.get("body") or "",
            reward=reward["amount"],
            currency=reward["currency"],
            url=item["html_url"],
            source="GitHub"
        )

        opportunities.append(opportunity)

    return opportunities
        