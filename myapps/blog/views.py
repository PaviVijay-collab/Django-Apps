from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.
def index(request):
    posts = [
        {'id': 1, "title": 'Business Blog', "content": 'Five Ways to Use Social Media for Business', 'tag': 'Business'},
        {'id': 2, "title": 'Fitness Blog', "content": 'The Top 5 Tips for Successful Bodybuilding', 'tag': 'Fitness'},
        {'id': 3, "title": 'Travel Blog', "content": 'Top 10 Budget Hotels in the USA', 'tag': 'Travel'},
        {'id': 4, "title": 'Startup Blog', "content": '15 Inspiring Blogs for Entrepreneurs', 'tag': 'Startup'},
    ]
    return render(request, 'blog/index.html', {'title': 'Lastest Posts', 'posts': posts})

def post_details(request, post_id, common_id):
    return render(request, 'blog/details.html')

def old_url_redirect(request):
    return redirect(reverse('blog:New Page'))

def new_url_view(request):
    return HttpResponse("Welcome To New Page")