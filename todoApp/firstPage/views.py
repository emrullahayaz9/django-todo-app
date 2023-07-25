from django.shortcuts import render
def firstPage(request):
    return render(request, "firstPage.html")