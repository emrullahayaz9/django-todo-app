from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.
@login_required(login_url="auth/login")
def todo(request):
    boolean=False
    
    if request.method=="GET":
        form = models.todoModelForm()
        return render(request, "todo.html", {"form":form})
    if request.method=="POST":
        form = models.todoModelForm(request.POST)
        if form.is_valid():
            header = request.POST["header"]
            content = request.POST["content"]
            models.todoModel(header=header, content=content).save()
            form = models.todoModelForm()
            data = models.todoModel.objects.all()
            return render(request, "todo.html", {"form":form, "data":data})
        else:
            boolean=True
            form = models.todoModelForm()
            error_message="form is not valid!"
            return render(request, "todo.html", {"form":form, "error_message":error_message, "boolean":boolean})