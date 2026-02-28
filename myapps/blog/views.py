import random

from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.urls import reverse
from django.db.models.functions import Random
from django.core.paginator import Paginator

# import models
from blog.models import Post
from blog.forms import ContactForm


import logging

# posts = [
#         {'id': 1, "title": 'Business Blog', "content": 'Five Ways to Use Social Media for Business', 'tag': 'Business'},
#         {'id': 2, "title": 'Fitness Blog', "content": 'The Top 5 Tips for Successful Bodybuilding', 'tag': 'Fitness'},
#         {'id': 3, "title": 'Travel Blog', "content": 'Top 10 Budget Hotels in the USA', 'tag': 'Travel'},
#         {'id': 4, "title": 'Startup Blog', "content": '15 Inspiring Blogs for Entrepreneurs', 'tag': 'Startup'},
#     ]

# Create your views here.
def index(request):
    # posts = Post.objects.all().order_by(Random())

    posts = Post.objects.all()

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/index.html', {'title': 'Lastest Posts', 'page_obj': page_obj})

def post_details(request, slug):

    # post = next((item for item in posts if item['id'] == int(post_id)), None)
    try:
        
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category=post.category).exclude(pk=post.id)

    # logger = logging.getLogger(__name__)
    # logger.debug(f'This is post data = {post}')
    
        return render(request, 'blog/details.html', {'post': post, 'related_posts': related_posts})
    
    except Post.DoesNotExist:
        raise Http404("Post Does Not Exist!")



def old_url_redirect(request):
    return redirect(reverse('blog:New Page'))

def new_url_view(request):
    return HttpResponse("Welcome To New Page")

def contact_us(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            logger = logging.getLogger("TESTING")
            logger.debug(f"Form Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['subject']} {form.cleaned_data['message']}")

    return render(request, 'blog/contact.html')