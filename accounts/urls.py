
from django.urls import path
from .views import LogIn, LogOut, Register

urlpatterns = [
    path('login', LogIn, name='LogIn'), # login o'rniga kirish deb yozish ham bo'ladi
    path('logout', LogOut, name='LogOut'), # logout o'rniga chiqish deb yozish ham bo'ladi
    path('register', Register, name='register')
]
