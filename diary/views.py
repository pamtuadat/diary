from django.shortcuts import render, redirect
from .models import Diary, Category
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib.auth import get_user_model, logout as auth_logout

User = get_user_model()

@login_required
def home_page(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    username = request.session.get('username')
    diaries = Diary.objects.filter(user=request.user)
    
    return render(request, "diary/index.html",{
        'username':username,
        'diaries': diaries,
        })

def setting_page(request):
    username = request.session.get('username')
    return render(request,"diary/settings.html",{'username':username})

@login_required
def write_diary_page(request):
    if request.method == "POST":
        title = request.POST.get('input-title')
        content = request.POST.get('input-content')

        diary = Diary.objects.create(
            user = request.user,
            title =title,
            content = content
        )

        diary.save()

        return redirect('index')
    return render(request,"diary/write_diary.html")

def analyze_page(request):
    username = request.session.get('username')
    return render(request, "diary/analyze.html",{'username':username})

def diary_detail_page(request):
    diary = Diary.objects.filter(user=request.user).last()
    return render(request, "diary/diary_detail.html")


def logout(request):
    auth_logout(request)
    return redirect('login')

def home_view(request):
    return render(request,'diary/home.html')