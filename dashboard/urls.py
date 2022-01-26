from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name="admin-dashboard"),

    path('users/', views.users_list_view, name="users-list"),
    path('teacher/create/', views.teacher_create_view, name="create-teacher"),

    path('assessments/', views.assessments_list_view, name="assessments-list"),
    path('assessments/create/<int:pk>/', views.assessments_create_view, name="assessments-create"),

    path('appointments/', views.appoint_list_view, name="appoint-list"),
    path('appointments/update/<int:pk>/<int:account_pk>/', views.AppointUpdateView.as_view(), name="appoint-update"),

]
