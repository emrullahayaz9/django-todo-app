from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login1, name='login1'),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
   
]
