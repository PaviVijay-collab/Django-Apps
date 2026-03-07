import random

from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.urls import reverse
from django.db.models.functions import Random
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail

# import models
from .models import Post, AboutUs
from .forms import ContactForm, RegisterForm, LoginForm, ForgotPasswordForm



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

        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        logger = logging.getLogger("TESTING")
        if form.is_valid():
            logger.debug(f"Form Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
            success_message = "Your Email has been sent"
            return render(request, 'blog/contact.html', {'form': form, 'success_message': success_message})

        else:
            logger.debug("Form Validation Failure")

        return render(request, 'blog/contact.html', {'form': form, 'name': name, 'email': email, 'message': message})

    return render(request, 'blog/contact.html')

def about_us(request):
    about_content = AboutUs.objects.first()
    if about_content is None or not about_content.content:
        about_content = "Default content goes here." #Default Text

    else:
        about_content = about_content.content

    return render(request, 'blog/about.html', {'about_content': about_content})

def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False) # user data create
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Registration Successfull, You Can log in.")
            return redirect(reverse("blog:Log in"))
        

    return render(request, 'blog/register.html', {'form': form})


def login(request):
    form = LoginForm()

    if request.method == 'POST':
        # login form
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                print("LOGIN SUCCESS")
                return redirect("blog:Dashboard") # redirect to dashboard
        
    return render(request, 'blog/login.html', {'form': form})


def dashboard(request):
    blog_title = 'My Posts'
    return render(request, 'blog/dashboard.html', {'title': blog_title})

def logout(request):
    auth_logout(request)
    return redirect('blog:Introduction')

def forgetpassword(request):
    form = ForgotPasswordForm()
    if request.method == "POST":
        form = ForgotPasswordForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)

            # send email to reset password
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            current_site = get_current_site(request) # 127.0.0.1:8000
            domain = current_site.domain
            subject = "Reset Password Requested"
            message = render_to_string('blog/resetpasswordemail.html', {
                'domain': domain,
                'uid': uid,
                'token': token
            })

            send_mail(subject, message, 'noreply@abc.com', [email])
            messages.success(request, "Email has been sent")

    return render(request, 'blog/forgotpassword.html', {'form': form})

def reset_password(request):
    pass