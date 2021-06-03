# Django
from django.shortcuts import redirect

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)
        statusCode = response.status_code

        if request.user.is_anonymous and statusCode==404:
            return redirect('login')

        if not request.user.is_anonymous and statusCode==404:
            return redirect('feed')

        return response