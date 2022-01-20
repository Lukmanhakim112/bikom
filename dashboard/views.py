from django.shortcuts import redirect, render
from django.contrib import messages


from .forms.forms import TeacherCreationForm

def dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html') 


def teacher_create_view(request):

    form = TeacherCreationForm(request.POST or None, request.FILES or None)

    if form.is_valid():

        account = form.save()
        account.is_staff = True
        account.save()

        messages.success(request, "Akun berhasil ditambahkan.")
        return redirect('admin-dashboard')

    ctx = {
        'form': form,
    }

    return render(request, 'dashboard/create_teacher.html', ctx)
