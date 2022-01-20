from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name="admin-dashboard"),
    path('create-teacher/', views.teacher_create_view, name="create-teacher"),
]
