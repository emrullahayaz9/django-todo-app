from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def login1(request):
    form = AuthenticationForm()
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            boolean = False
            login(request, user)
            return render(request, "success.html", {"username":username, "form":form, "user":user})
        else:
            boolean = True
            errorMessage = "username or password incorrect"
            return render(request, "base.html", {"errorMessage":errorMessage, "boolean":boolean, "form":form})

    else:
         return render(request, "login.html", {"form":form})

def register(request):
     if request.method=="GET":
        form = AuthenticationForm()
        return render(request, "base.html", {"form":form})
     elif request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect("login1")
     

def logout_view(request):
    logout(request)
    return render(request, "SuccessLogout.html")




