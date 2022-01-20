from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import UpdateView

from .forms.forms import TeacherCreationForm, AppointModelForm

from users.models import CustomUser

from students.models import AppointmentSchedule 

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

def appoint_list_view(request):

    # TODO: filter just certain teacher can see certain appointments 
    if request.user.is_superuser:
        appointments = AppointmentSchedule.objects.all() 
    else:
        appointments = AppointmentSchedule.objects.filter(teacher=request.user.pk) 


    return render(request, 'dashboard/appointment_list.html', {'appointments': appointments})


class AppointUpdateView(UpdateView):
    model = AppointmentSchedule
    form_class = AppointModelForm
    template_name = 'dashboard/appointmentschedule_update.html'
    success_url = reverse_lazy('appoint-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = CustomUser.objects.get(pk=self.kwargs.get("account_pk"))

        return context

