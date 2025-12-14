import email
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, alogin, alogout
from django.contrib.auth.decorators import login_required
from asgiref.sync import sync_to_async





@login_required(login_url="/login/")
async def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get("receipe_image")
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")

        print(receipe_description)
        print(receipe_image)
        print(receipe_name)

        await Receipe.objects.acreate(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description,
        )

        return redirect("/receipes/")
    queryset = Receipe.objects.all()

    if request.GET.get("search"):
        queryset = queryset.filter(receipe_name__icontains=request.GET.get("search"))
    
    # Convert queryset to list for async template rendering
    receipes_list = [receipe async for receipe in queryset]
    context = {"receipes": receipes_list}

    return render(request, "receipes.html", context)





async def update_receipe(request, id):
    queryset = await Receipe.objects.aget(id=id)
    if request.method == "POST":
        data = request.POST

        receipe_image = request.FILES.get("receipe_image")
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        await queryset.asave()
        return redirect("/receipes")
    context = {"receipe": queryset}
    return render(request, "update_receipes.html", context)


async def delete_receipe(request, id):
    queryset = await Receipe.objects.aget(id=id)
    await queryset.adelete()
    return redirect("/receipes/")


async def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = await sync_to_async(authenticate)(request, username=username, password=password)
        user_exists = await sync_to_async(User.objects.filter(username=username).exists)()
        
        if not user_exists:
            messages.error(request, "Invalid username")
            return redirect("/login/")
        # if not User.objects.filter(password=password).exists():
        #     messages.error(request, "Invalid password")
        #     return redirect("/login/")
        if user is not None:
            await alogin(request, user)
            return redirect("/receipes/")
            # messages.error(request, "Invalid Password")
            # return redirect("/login/")

        else:
            messages.error(request, "something wrong")
            return redirect("/login/")
            # login(request, user)
            # return redirect("/dashboard/")

    queryset = [user async for user in User.objects.all()]
    context = {"User": queryset}
    return render(request, "login.html", context)


async def logout_page(request):
    await alogout(request)
    return redirect('/login/')


async def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)

        user_exists = await sync_to_async(user.exists)()
        if user_exists:
            messages.info(request, "Username already taken")
            return redirect("/register/")

        user = await User.objects.acreate(
            first_name=first_name, last_name=last_name, username=username, email=email
        )
        await sync_to_async(user.set_password)(password)
        await user.asave()

        messages.info(request, "Account created Sucessfully")

        return redirect("/login/")

    return render(request, "register.html")


async def home(request):
    return render(request, "home.html")

async def admin_page(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get("receipe_image")
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")

        print(receipe_description)
        print(receipe_image)
        print(receipe_name)

        await Receipe.objects.acreate(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description,
        )

        return redirect("/receipes/")
    queryset = [receipe async for receipe in Receipe.objects.all()]
    
    return render(request, "admin_page.html")

async def password_reset_complete(request):
    return render(request, "password_reset_complete.html")
