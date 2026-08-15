import re
import os
from dotenv import load_dotenv
import requests

from app.collectors.github_issue import get_issue
from app.models.opportunity import Opportunity
from app.scoring.reward_parser import extract_reward
from app.scoring.skill_matcher import find_required_skills, calculate_skill_match


GITHUB_API = "https://api.github.com/search/issues"

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def find_opportunities():
    params = {
        "q": "label:bounty state:open",
        "sort": "updated",
        "order": "desc",
        "per_page": 20,
    }

    headers = {}

    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    response = requests.get(
        GITHUB_API,
        params=params,
        headers=headers,
        timeout=10,
    )

    response.raise_for_status()

    data = response.json()

    opportunities = []

    for item in data.get("items", []):
        parsed_url = parse_github_url(item["html_url"])

        if parsed_url is None:
            continue

        issue = get_issue(
            parsed_url["owner"],
            parsed_url["repo"],
            parsed_url["issue_number"],
        )

        body = issue.get("body") or ""
        required_skills = find_required_skills(body)
        skill_match = calculate_skill_match(required_skills)
        reward = extract_reward(issue["body"])

        if reward["amount"] is None:
            reward = extract_reward(issue["title"])
        

        opportunity = Opportunity(
            title=issue["title"],
            description=body,
            reward=reward["amount"],
            currency=reward["currency"],
            url=item["html_url"],
            source="GitHub",
            skills=required_skills,
            skill_match=skill_match
        )

        opportunities.append(opportunity)

    return opportunities


def parse_github_url(url):
    pattern = r"github\.com/([^/]+)/([^/]+)/issues/(\d+)"

    match = re.search(pattern, url)

    if not match:
        return None

    return {
        "owner": match.group(1),
        "repo": match.group(2),
        "issue_number": int(match.group(3)),
    }