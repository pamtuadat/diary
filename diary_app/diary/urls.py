from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home_page, name='home'),
    path('write_diary/',views.write_diary_page,name='write_diary'),
    path('analyze/',views.analyze_page,name='analyze'),
    path('setting/',views.setting_page,name='setting'),
    path('diary_detail/',views.diary_detail_page,name='diary_detail'),
    path('logout/', views.logout_view, name='logout'),
    
]