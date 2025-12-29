from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from diary.models import Diary
from django.db.models import Q
from django.utils import timezone

User = get_user_model()

# Create your views here.
@login_required
def dashboard_view(request):
    # tong so user
    users = User.objects.all()
    diaries = Diary.objects.all()

    username = request.session.get('username')
    email  = request.session.get('email')
    
    
    return render(request,"dashboard/dashboard.html",{
        'user_size':users.count(),
        'count_user_online':users.filter(is_active=True).count(),
        'count_diary':diaries.count(),
        'username':username,
        'email':email,
        'count_diary_today':diaries.filter(create_at= timezone.now().date()).count()
    })

@login_required
def users_view(request):
    role = request.GET.get('role', 'all')
    status = request.GET.get('status','all')
    word_key = request.GET.get('tim-kiem', '')

    users = User.objects.all()

    if role == 'admin':
        users = users.filter(is_staff=True)
    elif role == 'user':
        users = users.filter(is_staff=False)

    elif status == 'active':
        users = users.filter(is_active=True)
    elif status == "blocked":
        users = users.filter(is_active=False)

    if word_key:
        users = users.filter(
            Q(email__icontains=word_key) |
            Q(username__icontains=word_key)
        )


    # tong so user
    user_size = users.count()

    #phan trang
    paginator = Paginator(users, 5)

    default_page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(default_page_number)

    username = request.session.get('username')
    email  = request.session.get('email')
    
    return render(request, "dashboard/users.html",{
        'users':users,
        'user_size':user_size,
        'page_obj': page_obj,
        'username':username,
        'email':email,
        'word_key':word_key
    })

@login_required
def diaries_view(request):
    word_key = request.GET.get('tim-kiem','')
    word_find_user = request.GET.get('tim-user','')

    diaries = Diary.objects.all()

    username = request.session.get('username')
    email  = request.session.get('email')

    if word_key:
        diaries = diaries.filter(
            Q(id__icontains = word_key) |
            Q(title__icontains =word_key)
        )

    if word_find_user:
        diaries = diaries.filter(user__username__icontains = word_find_user)


    # diaries = diaries.order_by('-created_at')


    return render(request,"dashboard/diaries.html",{
        'diaries':diaries,
        'username':username,
        'email':email,
        'word_key':word_key
    })

@login_required
def reports_view(request):
    username = request.session.get('username')
    email  = request.session.get('email')

    diaries = Diary.objects.all()
    users = User.objects.all()

    return render(request,"dashboard/reports.html",{
        'username':username,
        'email':email,
        'count_diary': diaries.count(),
        'count_user_month':users.filter(date_joined__month=timezone.now().month,
                                        date_joined__year=timezone.now().year).count()
    })



def add_user(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        is_admin = request.POST.get("is_admin") == "on"

        user =User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        if is_admin:
            user.is_staff=True
            user.is_superuser=True

        user.save()

        return redirect('users')
    return redirect('users')








