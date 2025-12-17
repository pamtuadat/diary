from django.shortcuts import render, redirect
from .models import Diary, Category
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib.auth import logout



@login_required
def home_page(request):
    diary = Diary.objects.filter(user =request.user).last()

    return render(request, "diary/index.html",{'diary':diary})

def setting_page(request):
    diary = Diary.objects.filter(user=request.user).last()
    return render(request,"diary/settings.html",{'diary':diary})

def write_diary_page(request):
    return render(request,"diary/write_diary.html")

def analyze_page(request):
    diary = Diary.objects.filter(user=request.user).last()
    return render(request, "diary/analyze.html",{'diary':diary})

def diary_detail_page(request):
    diary = Diary.objects.filter(user=request.user).last()
    return render(request, "diary/diary_detail.html")


def logout_view(request):
    logout(request)
    return redirect('login')