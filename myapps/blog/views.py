from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello Everyone, Welcome To My Blog")


def post_details(request, postID):
    return HttpResponse(f"Here You Can Read the Details Of the Posts. And The Post ID is {postID}")