from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import RegisterFrom
from django.contrib import messages

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Email không tồn tại")
            return render(request, "accounts/login.html")

        user = authenticate(
            request,
            username=user.username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Sai mật khẩu")

    return render(request, "accounts/login.html")

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # kiem tra username co ton hai hay chua
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username đã tồn tại")
            return render(request, "accounts/register.html")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email đã tồn tại")
            return render(request, "accounts/register.html")
        
        user = User.objects.create_user(
            username = username,
            email =email,
            password =password
        )

        user.save()

        return redirect('login')

    return render(request, "accounts/register.html")

