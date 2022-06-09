from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegisterForm

def Home(request):
    return render(request,'home.html')

def LogIn(request):
    if request.method == 'POST':

        # html formadan data larni olish
        username = request.POST.get('username')
        password = request.POST.get('password')

        # authenticate orqali tekshiramiz
        user = authenticate(username=username, password=password)

        if user:
            # user mavjud bolsa login qilinadi
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "Username or Password is incorrect")
            return redirect('LogIn')

    return render(request, 'login.html')

def Register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() # userni ro'yxatga olish
            login(request, user) # login qilish
            messages.success(request, 'Your account has been created!')
            return redirect('home')
        else:
            messages.warning(request, form.errors)
            return redirect('register')

    return render(request, 'register.html')

def LogOut(request):
    logout(request)
    return redirect('LogIn')