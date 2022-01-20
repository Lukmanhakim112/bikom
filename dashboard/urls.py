from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name="admin-dashboard"),

    path('users/', views.users_list_view, name="users-list"),
    path('teacher/create/', views.teacher_create_view, name="create-teacher"),

]
