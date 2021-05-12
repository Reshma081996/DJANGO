from django.shortcuts import render,redirect

# Create your views here.
from .forms import BookCreateForm,UserRegForm,UserLoginForm
from .models import Book
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
def register(request):
    form=UserRegForm()
    context={}
    context['form']=form
    if request.method=="POST":
        form=UserRegForm(request.POST)
        if form.is_valid():

            form.save()
            return render(request,"book/login.html")
        else:
            form = UserRegForm(request.POST)

            context['form'] = form
            return render(request, "book/registeration.html", context)
    return render(request,"book/registeration.html",context)


def lo_login(request):
    form=UserLoginForm()
    context={}
    context['form']=form
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
           username=form.cleaned_data.get("username")
           password = form.cleaned_data.get("password")
           print(username,password)
           user=authenticate(request,username=username,password=password)
           if user:
               print("login sucess")
               login(request, user)
               return redirect("create")
           else:
               print("login failed")
               return render(request, "book/login.html", context)
        else:
            print("hello")
            form = UserRegForm(request.POST)
            return render(request, "book/login.html", context)
    return render(request,"book/login.html",context)

def lo_logout(request):
        logout(request)
        return redirect("create")



def book_create(request):
    form=BookCreateForm()
    context= {}
    context['form']=form
    #context={form:form,books:books}
    books=Book.objects.all()
    context["books"]=books
    if request.method=="POST":
        form=BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            print("book objt saved")
            return redirect("create")
            # book_name=form.cleaned_data.get("book_name")
            # author= form.cleaned_data.get("author")
            # price = form.cleaned_data.get("price")
            # pages = form.cleaned_data.get("pages")
            # category=form.cleaned_data.get("category")
            # book=Book(book_name=book_name,author=author,price=price,pages=pages,category=category)
            # book.save()
            # print("book object saved")
            # return redirect("create")
        else:
            form = BookCreateForm(request.POST)
            context['form'] = form
            return render(request, "book/bookcreate.html", context)

    return render(request,"book/bookcreate.html",context)

def book_delete(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect("create")


def book_detail(request,id):
    book=Book.objects.get(id=id)
    context={}
    context["book"]=book
    return render(request,"book/bookdetail.html",context)


def book_update(request,id):
    book = Book.objects.get(id=id)
    form = BookCreateForm(instance=book)
    context = {}
    context["form"] = form
    if request.method=="POST":
        form= BookCreateForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            print("book objt saved")
            return redirect("create")
        else:
            form=BookCreateForm(request.POST)
            context={}
            context['form']=form
            return render(request, "book/bookedit.html", context)


    return render(request, "book/bookedit.html", context)

# def book_Search(request,author):
#     book=Book.objects.get(author=author)
#     context={}
#     context['book']=book
#     return render(request, "book/bookdetail.html", context)

