from django.core.cache import cache
from .models import Visit

def cache_visit(request):
    visiter = {
        'user': request.user, 
        'path': request.path, 
        'method': request.method
    }
    print(cache.get('visits'))
    print(1)
    if cache.get('visits') is not None:
        visits = [*cache.get('visits'), visiter]
        return cache.set('visits', visits, 3600)
    else:
        return cache.set('visits', [visiter], 3600)

def save_visit():
    if cache.get('visits') is not None:
        visiters = cache.get('visits')
        cache.delete('visits')
        for visiter in visiters:
            if visiter['user'].is_authenticated:
                user = visiter['user']
            else:
                user = None
            Visit.objects.create(
                user=user,
                url=visiter['path'],
                method=visiter['method']
            )