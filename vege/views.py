import email
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required





@login_required(login_url="/login/")
def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get("receipe_image")
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")

        print(receipe_description)
        print(receipe_image)
        print(receipe_name)

        Receipe.objects.create(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description,
        )

        return redirect("/receipes/")
    queryset = Receipe.objects.all()

    if request.GET.get("search"):
        queryset = queryset.filter(receipe_name__icontains=request.GET.get("search"))
    context = {"receipes": queryset}

    return render(request, "receipes.html", context)





def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST

        receipe_image = request.FILES.get("receipe_image")
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect("/receipes")
    context = {"receipe": queryset}
    return render(request, "update_receipes.html", context)


def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect("/receipes/")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid username")
            return redirect("/login/")
        # if not User.objects.filter(password=password).exists():
        #     messages.error(request, "Invalid password")
        #     return redirect("/login/")
        if user is not None:
            login(request, user)
            return redirect("/receipes/")
            # messages.error(request, "Invalid Password")
            # return redirect("/login/")

        else:
            messages.error(request, "something wrong")
            return redirect("/login/")
            # login(request, user)
            # return redirect("/dashboard/")

    queryset = User.objects.all()
    context = {"User": queryset}
    return render(request, "login.html", context)


def logout_page(request):
    logout(request)
    return redirect('/login/')


def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already taken")
            return redirect("/register/")

        user = User.objects.create(
            first_name=first_name, last_name=last_name, username=username,email=email
        )
        user.set_password(password)
        user.save()

        messages.info(request, "Account created Sucessfully")

        return redirect("/login/")

    return render(request, "register.html")


def home(request):
    return render(request, "home.html")

def admin_page(request):
    
    return render(request, "admin_page.html")
def password_reset_complete(request):
    return render(request,"password_reset_complete.html")
