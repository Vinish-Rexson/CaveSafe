from django.shortcuts import render, redirect
from django.contrib import messages
from math import ceil
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, "home.html")


def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def kgf(request):
    return render(request, "kgf.html")


def form(request):
    return render(request, "form.html")


def bugs(request):
    return render(request, "bugs.html")


def geo(request):
    return render(request, "geo.html")


def emerg(request):
    return render(request, "emerg.html")


def chat(request):
    return render(request, "chat.html")

@login_required(login_url="/login")
def profile(request):
    id = request.user.id
    if request.method == "GET":
        data = Profile.objects.filter(user_id=id).exists()
        print(data)
        if data :
            return redirect("/geo")
        else:
            data={'id':id,}
            return render(request, "form.html", data)
    if request.method == "POST":
        name = request.POST.get("name")
        image = request.POST.get("image")
        dob = request.POST.get("dob")
        address = request.POST.get("address")
        phone_no = request.POST.get("phone_no")
        allergies = request.POST.get("allergies")
        current_medications = request.POST.get("current_medications")
        blood_group = request.POST.get("blood_group")
        desc = request.POST.get("desc")
        user_id = request.POST.get("user_id")

        Comp_Pro = Profile(
            name=name,
            image=image,
            desc=desc,
            date_of_birth=dob,
            address=address,
            phone_no=phone_no,
            allergies=allergies,
            current_medications=current_medications,
            blood_group=blood_group,
            user_id=user_id,
        )
        Comp_Pro.save()
        messages.info(request, "Profile Completed")
        return redirect("/geo")
    
