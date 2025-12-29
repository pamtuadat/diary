from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.dashboard_view, name="admin"),
    path('users/', views.users_view, name="users"),
    path('diaries/', views.diaries_view, name="diaries"),
    path('reports/', views.reports_view, name="reports"),
    path('users/add/', views.add_user, name="add_user"),
]