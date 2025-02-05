from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome to the home page!")
def students(request):
    return HttpResponse("Welcome to the Students page!")


def teachers(request):
    return HttpResponse("Welcome to the teachers page!")