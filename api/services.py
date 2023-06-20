from .models import Visit
from django.contrib.auth.models import AnonymousUser

class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        response = self.get_response(request)
        if not isinstance(request.user, AnonymousUser):
            user = request.user
        else:
            user = None
        Visit.objects.create(
            user=user,
            url=request.path,
            method=request.method
        )
        return response