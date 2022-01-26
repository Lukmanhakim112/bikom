import random

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from students.forms.forms import (
    StudentProfileForm, FatherModelForm, 
    MotherModelForm, BestFriendsModelForm,
    AppointmentModelForm
)
from students.models import (
    AppointmentSchedule, StudentProfile, FatherStudentModels,
    MotherStudentModels, BestFriendsModel
)

from users.models import CustomUser
from users.decorators import redirect_staff


@login_required()
@redirect_staff
def student_dashboard(request):

    try:
        s_profile = StudentProfile.objects.get(account=request.user) 
    except ObjectDoesNotExist:
        return redirect('student-profile')

    color = "#"+"".join([random.choice('0123456789ABCDEF') for _ in range(6)])

    f_friend = BestFriendsModelForm()
    friends = BestFriendsModel.objects.filter(friend=request.user.pk)

    appointments = AppointmentSchedule.objects.filter(student=request.user.pk)


    ctx = {
        "color": color,
        "s_profile": s_profile,
        "f_friend": f_friend,
        "friends": friends,
        "appointments": appointments,
        "a_form": AppointmentModelForm(),
    }

    return render(request, 'students/student_dashboard.html', ctx)


@login_required()
@redirect_staff
def student_profile(request):

    try:
        profile = StudentProfile.objects.get(account=request.user.pk)
    except ObjectDoesNotExist:
        profile = None

    try:
        father = FatherStudentModels.objects.get(child=request.user.pk)
    except ObjectDoesNotExist:
        father = None

    try:
        mother = MotherStudentModels.objects.get(child=request.user.pk)
    except ObjectDoesNotExist:
        mother = None

    p_form = StudentProfileForm(instance=profile)
    f_form = FatherModelForm(instance=father)
    m_form = MotherModelForm(instance=mother)

    if request.method == 'POST':
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


@login_required()
def student_best_friends(request):

    # Only accept POST method
    if request.method != "POST":
        return redirect('student-dashboard')

    form = BestFriendsModelForm(request.POST)
    
    if form.is_valid():

        full_name = form.cleaned_data.get("full_name")
        phone_number = form.cleaned_data.get("phone_number")

        obj, _ = BestFriendsModel.objects.get_or_create(
            phone_number=phone_number,
            defaults={"full_name": full_name, "phone_number": phone_number}
        )
        obj.friend.add(request.user)

        messages.success(request, 'Teman dekat berhasil disimpan.')
        return redirect('student-dashboard')

    messages.warning(request, 'Data yang diinputkan tidak valid.')
    return redirect('student-dashboard')

@login_required()
@redirect_staff
def student_appointment(request):

    form = AppointmentModelForm(request.POST)

    if form.is_valid():
        form.instance.student = request.user
        form.save()

        messages.success(request, 'Jadwal bimbingan berhasil disimpan, menunggu persetujuan guru BK.')
        return redirect('student-dashboard')

    messages.warning(request, 'Data yang diinputkan tidak valid.')
    return redirect('student-dashboard')




