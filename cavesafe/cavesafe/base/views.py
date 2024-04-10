from django.shortcuts import render, redirect
from django.contrib import messages
from math import ceil
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Profile


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


def profile(request):
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
        )
        Comp_Pro.save()
        messages.info(request, "Profile Completed")
        return redirect("/home")

    return render(request, "form.html")
