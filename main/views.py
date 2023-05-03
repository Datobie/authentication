from django.shortcuts import render
from . forms import UserRegistrationForm
from django.http import HttpResponse

# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("You ahve been created successfully")


    else:
        form = UserRegistrationForm()

    context = {
        "form": form
    }

    return render(request, "main/register.html", context)


def home_page(request):
    return render(request, "main/home.html")