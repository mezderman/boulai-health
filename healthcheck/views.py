from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

def health_check(request):
    logger.info("Health check endpoint hit")
    return JsonResponse({"status": "OK"}, status=200)
