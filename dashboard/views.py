from django.shortcuts import get_list_or_404, redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import UpdateView, DeleteView

from .forms.forms import TeacherCreationForm, AppointModelForm

from users.models import CustomUser

from assessments.models import AnswerModel, AssesmentModel, QuestionModel
from assessments.forms import (
    AssesmentModelForm, QuestionModelForm,
    AnswerFormset, AnswerFormHelper, UpdateAnswerFormset
)

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

def assessments_list_view(request):

    assessments = AssesmentModel.objects.all()
    a_form = AssesmentModelForm()

    if request.method == 'POST':
        a_form = AssesmentModelForm(request.POST)
        if a_form.is_valid():
            a_form.save()

    ctx = {
        'assessments': assessments,
        'a_form': a_form,
    }

    return render(request, 'dashboard/assessments_list.html', ctx)

def assessments_detail_view(request, pk):

    question = get_list_or_404(QuestionModel, assessment=pk)
    asment = question[0].assessment

    ctx = {
        'question_list': question,
        'asment': asment,
    }

    return render(request, 'dashboard/question_list.html', ctx)

def question_create_view(request, pk):
    asment = get_object_or_404(AssesmentModel, pk=pk)
    question_counter = QuestionModel.objects.all().count()

    q_form = QuestionModelForm(request.POST or None, request.FILES or None)
    a_form = AnswerFormset(request.POST or None, request.FILES or None)
    form_helper = AnswerFormHelper()

    if q_form.is_valid() and a_form.is_valid():
        q_form.instance.assessment = asment
        question = q_form.save()

        for answer in a_form:
            AnswerModel.objects.create(
                answer=answer.cleaned_data.get("answer"),
                answer_img=answer.cleaned_data.get("answer_img"),
                question=question,
            )

        return redirect('question-create', pk=asment.pk)

    ctx = {
        'q_form': q_form,
        'a_form': a_form,
        'form_helper': form_helper,
        'asment': asment,
        'question_counter': question_counter,
    }

    return render(request, 'dashboard/assessment_create.html', ctx)

def question_update_view(request, pk):
    question = get_object_or_404(QuestionModel, pk=pk)
    answer = AnswerModel.objects.filter(question=question.pk).values('pk', 'answer', 'answer_img')

    q_form = QuestionModelForm(request.POST or None, request.FILES or None, instance=question)
    a_form = UpdateAnswerFormset(request.POST or None, request.FILES or None, initial=list(answer))
    form_helper = AnswerFormHelper()

    if q_form.is_valid() and a_form.is_valid():
        q_form.save()

        for a in a_form:
            AnswerModel.objects.filter(pk=a.cleaned_data.get('pk')).update(
                answer=a.cleaned_data.get('answer'),
                answer_img=a.cleaned_data.get('answer_img')
            )

        return redirect('assessments-detail', pk=question.assessment.pk) 

    ctx = {
        'q_form': q_form,
        'a_form': a_form,
        'form_helper': form_helper,
        'answer': answer,
    }

    return render(request, 'dashboard/question_update.html', ctx)

class QuestionDeleteView(DeleteView):
    model = QuestionModel

    def get_success_url(self):
        pk = self.kwargs.get("asmentpk")
        return reverse_lazy('assessments-detail', kwargs = {'pk': pk})

class AppointUpdateView(UpdateView):
    model = AppointmentSchedule
    form_class = AppointModelForm
    template_name = 'dashboard/appointmentschedule_update.html'
    success_url = reverse_lazy('appoint-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = CustomUser.objects.get(pk=self.kwargs.get("account_pk"))

        return context

