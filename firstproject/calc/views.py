from django.shortcuts import render

# Create your views here.
def getcalc(request):
    return render(request,"calculation/calculation.html")

def solve(request):
    num1=int(request.POST.get("num1"))
    num2 = int(request.POST.get("num2"))
    add=num1+num2
    print(add)
    context={}
    context['res']=add
    return render(request,"calculation/calculation.html",context)