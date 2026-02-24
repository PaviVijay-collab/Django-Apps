from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {'title': 'Lastest Posts'})


def post_details(request, post_id):
    return render(request, 'blog/details.html')


def old_url_redirect(request):
    return redirect(reverse('blog:New Page'))

def new_url_view(request):
    return HttpResponse("Welcome To New Page")