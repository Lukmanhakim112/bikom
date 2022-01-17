from django.urls import path

from . import views

urlpatterns = [
    path('', views.student_dashboard, name="student-dashboard"),
    path('profile/', views.student_profile, name="student-profile"),
]
