from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from crispy_forms.helper import FormHelper

from .forms_layout import (
    STUDENT_REGIS_FORM_LAYOUT,
    STUDENT_PROFILE_FORM_LAYOUT,
    parent_form_layout,
    BEST_FRIEND_FORM_LAYOUT,
    APPOINTMENT_FORM_LAYOUT,
)
from students.models import (
    StudentProfile, FatherStudentModels,
    MotherStudentModels, BestFriendsModel,
    AppointmentSchedule,
)

from users.models import CustomUser


class StudentRegisForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = STUDENT_REGIS_FORM_LAYOUT

    class Meta:
        model = CustomUser
        fields = [
            'username', 'full_name', 'phone_number',
            'photo', 'password1', 'password2'
        ]

class StudentProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = STUDENT_PROFILE_FORM_LAYOUT
        self.helper.form_tag = False
        self.helper.disable_csrf = True

    class Meta:
        model = StudentProfile
        exclude = ['account']

class FatherModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = parent_form_layout("father")
        self.helper.form_tag = False
        self.helper.disable_csrf = True

    class Meta:
        model = FatherStudentModels
        exclude = ['child']

class MotherModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = parent_form_layout("mother")
        self.helper.form_tag = False
        self.helper.disable_csrf = True

    class Meta:
        model = MotherStudentModels
        exclude = ['child']

class BestFriendsModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = BEST_FRIEND_FORM_LAYOUT
        self.helper.form_id = "bestFriendForm"
        self.helper.form_action = reverse_lazy('student-best-save')

    class Meta:
        model = BestFriendsModel
        exclude = ['friend']

class AppointmentModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = APPOINTMENT_FORM_LAYOUT
        self.helper.form_id = "appointmentForm"
        self.helper.form_action = reverse_lazy('student-appointment-save')

    class Meta:
        model = AppointmentSchedule
        exclude = ['student', 'approved']



