from rest_framework.response import Response
from rest_framework.decorators import api_view

from app.collectors.github import find_opportunities

@api_view(["GET"])
def opportunities_list(request):
    opportunities = find_opportunities()

    data = []

    for opportunity in opportunities:
        data.append({
            "title": opportunity.title,
            "description": opportunity.description,
            "reward": opportunity.reward,
            "currency": opportunity.currency,
            "url": opportunity.url,
            "source": opportunity.source,
            "skills": opportunity.skills,
            "skill_match": opportunity.skill_match
        })

    return Response(data)