from django.urls import path
from .views import firstPage

urlpatterns = [
    path('', firstPage)
]
