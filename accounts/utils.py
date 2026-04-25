from django.shortcuts import redirect
from urllib.parse import urlencode

def login_required(func):
    def inner(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)

        login_url = '/accounts/login/'
        params = urlencode({'next': request.path})

        return redirect(f'{login_url}?{params}')

    return inner