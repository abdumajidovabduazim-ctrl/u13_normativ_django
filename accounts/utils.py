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


from threading import Thread
from django.core.mail import send_mail


def send_email_thread(subject, message, recipient_list):
    def send():
        send_mail(
            subject,
            message,
            'abdumajidovabduazim@gmail.com',
            recipient_list,
            fail_silently=False,
        )

    Thread(target=send).start()