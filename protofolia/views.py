from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "about.html")


def experience(request):
    return render(request, "experience.html")


def education(request):
    return render(request, "education.html")


def skills(request):
    return render(request, "skills.html")


def interests(request):
    return render(request, "interest.html")


def awards(request):
    return render(request, "awards.html")