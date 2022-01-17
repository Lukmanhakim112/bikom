import random

from django.shortcuts import render, redirect

from students.forms.forms import StudentProfileForm, FatherModelForm, MotherModelForm
from students.models import StudentProfile, FatherStudentModels, MotherStudentModels

from users.models import CustomUser


def student_dashboard(request):
    # TODO: redirect to staff dashboard
    if request.user.is_staff:
        pass

    try:
        s_profile = StudentProfile.objects.get(account=request.user) 
    except StudentProfile.DoesNotExist:
        return redirect('student-profile')

    color = "#"+"".join([random.choice('0123456789ABCDEF') for _ in range(6)])
    ctx = {
        "color": color,
    }

    return render(request, 'students/student_dashboard.html', ctx)


def student_profile(request):
    try:
        profile = StudentProfile.objects.get(account=request.user.pk)
        father = FatherStudentModels.objects.get(child=request.user.pk)
        mother = MotherStudentModels.objects.get(child=request.user.pk)
    except (StudentProfile.DoesNotExist, FatherModelForm.DoesNotExist, MotherModelForm.DoesNotExist):
        profile = None
        father = None
        mother = None

    p_form = StudentProfileForm(request.POST or None, instance=profile)
    f_form = FatherModelForm(request.POST or None, instance=father)
    m_form = MotherModelForm(request.POST or None, instance=mother)

    if p_form.is_valid() and f_form.is_valid() and m_form.is_valid():
        account = CustomUser.objects.get(pk=request.user.pk)

        p_form.instance.account = account
        m_form.instance.child = account
        f_form.instance.child = account

        p_form.save()
        m_form.save()
        f_form.save()

        return redirect('student-dashboard')

    ctx = {
        "form": p_form,
        "f_form": f_form,
        "m_form": m_form,
    }

    return render(request, 'students/student_profile.html', ctx)




