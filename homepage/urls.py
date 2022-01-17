from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name="homepage"),
    path('register/', views.student_regis, name="register"),
]
