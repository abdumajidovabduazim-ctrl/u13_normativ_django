import logging
from django.utils import timezone


logger = logging.getLogger('request_logger')


class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):


        url = request.path
        ip = request.META.get('REMOTE_ADDR', '')
        user = request.user
        vaqt = timezone.now().strftime('%Y-%m-%d %H:%M')

        log_yozuv = f"[{vaqt}] User: {user} | IP: {ip} | Path: {url}"
        logger.info(log_yozuv)


        response = self.get_response(request)

        return response