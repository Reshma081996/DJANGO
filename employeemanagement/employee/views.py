from django.shortcuts import render,redirect
from employee.forms import EmployeeCreateForm
from employee.models import Employee


# Create your views here.
#employee create
def create_employee(request):
    form=EmployeeCreateForm()
    context={}
    context['form']=form
    if request.method=="POST":
        form=EmployeeCreateForm(request.POST)
        if form.is_valid():
            empname=form.cleaned_data.get("name")
            designation=form.cleaned_data.get("designation")
            salary=form.cleaned_data.get("salary")
            location=form.cleaned_data.get("location")
            email=form.cleaned_data.get("email")
            print(empname,designation,salary,location,email)
            employee=Employee(name=empname,designation=designation,salary=salary,location=location,email=email)
            employee.save()
            print("saved")
            return redirect("listall")
    return render(request,"employee/create_employee.html",context)


#list all employee
def listall_employee(request):
    #orm query for listing all
    employees=Employee.objects.all()
    context = {}
    context['employees'] = employees
    return render(request, "employee/list_employee.html", context)


#view by id
def emp_detail(request,id):
    employee=Employee.objects.get(id=id)
    context={}
    context['employee']=employee
    return  render(request,"employee/detail.html",context)


# update
def update(request, id):
    employee = Employee.objects.get(id=id)
    emp={
        "name":employee.name,
        "designation":employee.designation,
        "salary":employee.salary,
        "location":employee.location,
        "email":employee.email

    }
    form=EmployeeCreateForm(initial=emp)
    context={}
    context['form']=form
    if request.method=="POST":
        form = EmployeeCreateForm(request.POST)
        if form.is_valid():
            empname = form.cleaned_data.get("name")
            designation = form.cleaned_data.get("designation")
            salary = form.cleaned_data.get("salary")
            location = form.cleaned_data.get("location")
            email = form.cleaned_data.get("email")
            print(empname, designation, salary, location, email)
            employee.name=empname
            employee.designation=designation
            employee.salary=salary
            employee.location=location
            employee.email=email
            employee.save()
            print("saved")
            return redirect("listall")
    return render(request,"employee/update.html",context)

def delete(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return render(request, "employee/list_employee.html", context)