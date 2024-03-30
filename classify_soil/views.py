from django.shortcuts import render
from rest_framework.response import Response
def index(request):
    return Response('hello this is my api for django')
