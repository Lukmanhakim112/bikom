from django import forms
from django.contrib.auth.forms import UserCreationForm

from crispy_forms.helper import FormHelper

from users.models import CustomUser

from students.models import AppointmentSchedule

from .forms_layout import (
    TEACHER_CREATION_FORM_LAYOUT,
    APPOINT_FORM_LAYOUT,
) 


class TeacherCreationForm(UserCreationForm):
    is_staff = forms.BooleanField(label="Status Staff", initial=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = "my-3"
        self.helper.form_id = "teacherCreationForm"
        self.helper.layout = TEACHER_CREATION_FORM_LAYOUT

    class Meta:
        model = CustomUser
        fields = [
            'username', 'full_name', 'phone_number',
            'photo', 'password1', 'password2', 'is_staff',
        ]

class AppointModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = "my-3"
        self.helper.form_id = "appointUpdateForm"
        self.helper.layout = APPOINT_FORM_LAYOUT

    class Meta:
        model = AppointmentSchedule
        exclude = ['teacher', 'student']


