from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def faculty_register(request):
    return HttpResponse("<h1> welcome to faculty registration page</h1")


def faculty_login(request):
    return HttpResponse("<h1> welcome to faculty login page</h1")

def faculty_timetable(request):
    return HttpResponse("<h1>timetable</h1")

def read_feedback(request):
    return HttpResponse("<h1> read feedback</h1")