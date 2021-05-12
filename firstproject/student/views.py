from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from student.forms import StudentRegistrationForm,loginform
# http methods-get(load corresponding html page), post(we have to store that data)

def registration (request):
    form=StudentRegistrationForm()
    context={}
    context["form"]=form
    if (request.method=="POST"):
            form=StudentRegistrationForm(request.POST)
            if form.is_valid():
                name=form.cleaned_data.get("name")
                email=form.cleaned_data.get("email")
                course=form.cleaned_data.get("course")
                phone=form.cleaned_data.get("phone")
                username=form.cleaned_data.get("username")
                password=form.cleaned_data.get("password")
                print(name,email,course,phone,username,password)
                # student=Student(name=name,email=email,course=course,phone=phone,username=username,password=password)
                print(student)
                return render(request, "student/registration.html", context)


    return render(request,"student/registration.html",context)

def login(request):
    form=loginform()
    context={}
    context['loginform']=form

    if request.method=="POST":
        form=loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            print(username,password)
            return render(request, "student/login.html", context)
    return render(request, "student/login.html", context)

#
#
# def stud_register(request):
#     return render(request,"student/studreg.html")
#
#
# def registration(request):
#     name=int(request.POST.get("name"))
#     email=request.POST.get("email")
#     course=request.POST.get("course")
#     print(name,course,email)
#     return render(request, "student/studreg.html")
#
#
# def stud_login(request):
#     return render(request,"student/studlogin.html")
#
# def timetable(request):
#     return HttpResponse("<h1>timetable</h1")
#
# def post_feedback(request):
#     return HttpResponse("<h1> post ur feedback</h1")