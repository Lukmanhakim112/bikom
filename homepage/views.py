from django.shortcuts import render

from students.forms.forms import StudentRegisForm


def index(request):
    return render(request, 'homepage/index.html')

def student_regis(request):

    form = StudentRegisForm()

    if request.method == 'POST':
        form = StudentRegisForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

    ctx = {
        'form': form,
    }

    return render(request, 'homepage/register_student.html', ctx)
