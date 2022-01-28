from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name="admin-dashboard"),

    path('users/', views.users_list_view, name="users-list"),
    path('teacher/create/', views.teacher_create_view, name="create-teacher"),

    path('assessments/', views.assessments_list_view, name="assessments-list"),
    path('assessments/detail/<int:pk>/', views.assessments_detail_view, name="assessments-detail"),

    path('assessments/question/create/<int:pk>/', views.question_create_view, name="question-create"),
    path('assessments/question/update/<int:pk>/', views.question_update_view, name="question-update"),
    path('assessments/question/delete/<int:pk>/<int:asmentpk>/', views.QuestionDeleteView.as_view(), name="question-delete"),

    path('appointments/', views.appoint_list_view, name="appoint-list"),
    path('appointments/update/<int:pk>/<int:account_pk>/', views.AppointUpdateView.as_view(), name="appoint-update"),

]
