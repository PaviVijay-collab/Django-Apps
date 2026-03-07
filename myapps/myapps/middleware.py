from django.urls import reverse
from django.shortcuts import redirect


class RedirectAuthenticatedMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        print("RedirectAuthenticatedMiddleware")
        # Check the user is Authenticated
        if request.user.is_authenticated:
            # List of path to check
            paths_to_redirect = [
                reverse('blog:Log in'),
                reverse('blog:Register Form')
            ]

            if request.path in paths_to_redirect:
                return redirect(reverse('blog:Introduction')) # Redirect to Homepage

        response = self.get_response(request)
        return response
    

class RestrictUnauthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("RestrictUnauthenticatedUserMiddleware")
        restricted_path = [reverse('blog:Dashboard')]

        if not request.user.is_authenticated and request.path in restricted_path:
            return redirect(reverse('blog:Log in'))
        
        response = self.get_response(request)
        return response



