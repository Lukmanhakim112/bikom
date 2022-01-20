from django.shortcuts import redirect, render
from django.contrib import messages


from .forms.forms import TeacherCreationForm
from users.models import CustomUser

def dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html') 


def teacher_create_view(request):

    form = TeacherCreationForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

        messages.success(request, "Akun berhasil ditambahkan.")
        return redirect('admin-dashboard')

    ctx = {
        'form': form,
    }

    return render(request, 'dashboard/create_teacher.html', ctx)

def users_list_view(request):

    users = CustomUser.objects.all()

    staff_user = users.filter(is_staff=True, is_superuser=False)
    student_user = users.filter(is_staff=False)

    ctx = {
        "staff_user": staff_user,
        "student_user": student_user,
    }

    return render(request, 'dashboard/users_list.html', ctx)




