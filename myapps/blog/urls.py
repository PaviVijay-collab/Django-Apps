from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="Introduction"),
    path("post/<str:slug>", views.post_details, name="Post Details"),
    path("new_url", views.new_url_view, name="New Page"),
    path('old_url', views.old_url_redirect, name="Old Page"),
    path('contact_us', views.contact_us, name="Contact Us"),
    path('about_us', views.about_us, name='About Us'),
    path('register', views.register, name="Register Form")
]