from django.http import JsonResponse

from .config import LEAGUE_ID

from .services.sleeper_service import get_league


def health(request):
    return JsonResponse({
        "status": "ok"
    })


def league(request):
    league_data = get_league(LEAGUE_ID)
    return JsonResponse(league_data)