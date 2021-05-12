
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def loadpage(request):
    return render(request,"prime/prime_check.html")

def check(request):
    number = int(request.POST.get("num"))
    flag=0
    for i in range (2,number):
        if (number%i==0):
            flag=flag+1
        else:
            pass
    if flag==0:
        print(number,"is prime")
    else:
        print(number," is not prime")


    return render(request, "prime/prime_check.html")










