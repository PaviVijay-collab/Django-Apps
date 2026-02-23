from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="Introduction"),
    path("post/<str:post_id>", views.post_details, name="Post Details"),
]