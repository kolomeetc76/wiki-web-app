from django.http import HttpResponseRedirect
from django.urls import reverse

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            # Если пользователь не аутентифицирован, перенаправляем его на страницу входа
            return HttpResponseRedirect(reverse('main/login.html'))  # Замените 'login' на ваш URL для страницы входа
        response = self.get_response(request)
        return response