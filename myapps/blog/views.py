from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.urls import reverse

# import models
from blog.models import Post


import logging

# posts = [
#         {'id': 1, "title": 'Business Blog', "content": 'Five Ways to Use Social Media for Business', 'tag': 'Business'},
#         {'id': 2, "title": 'Fitness Blog', "content": 'The Top 5 Tips for Successful Bodybuilding', 'tag': 'Fitness'},
#         {'id': 3, "title": 'Travel Blog', "content": 'Top 10 Budget Hotels in the USA', 'tag': 'Travel'},
#         {'id': 4, "title": 'Startup Blog', "content": '15 Inspiring Blogs for Entrepreneurs', 'tag': 'Startup'},
#     ]

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'title': 'Lastest Posts', 'posts': posts})

def post_details(request, slug):

    # post = next((item for item in posts if item['id'] == int(post_id)), None)
    try:
        post = Post.objects.get(slug=slug)

    # logger = logging.getLogger(__name__)
    # logger.debug(f'This is post data = {post}')
    
        return render(request, 'blog/details.html', {'post': post})
    
    except Post.DoesNotExist:
        raise Http404("Post Does Not Exist!")



def old_url_redirect(request):
    return redirect(reverse('blog:New Page'))

def new_url_view(request):
    return HttpResponse("Welcome To New Page")