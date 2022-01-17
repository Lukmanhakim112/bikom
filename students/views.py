import random

from django.shortcuts import render

from students.forms.forms import StudentProfileForm, FatherModelForm, MotherModelForm




def student_dashboard(request):
    color = "#"+"".join([random.choice('0123456789ABCDEF') for _ in range(6)])

    ctx = {
        "color": color,
    }

    return render(request, 'students/student_dashboard.html', ctx)


def student_profile(request):
    ctx = {
        "form": StudentProfileForm(),
        "f_form": FatherModelForm(),
        "m_form": MotherModelForm(),
    }

    return render(request, 'students/student_profile.html', ctx)
