from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    HTML,
    Div,
    Field,
    Layout,
    Row,
)
from crispy_forms.bootstrap import AppendedText, PrependedText

from .models import (
    AssesmentModel,
    QuestionModel,
    AnswerModel,
)

class AssesmentModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "assessmentCreationForm"

    class Meta:
        model = AssesmentModel
        fields = "__all__"

class QuestionModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Div('question', css_class="col-12"),
                Div(Field('img_question', css_class='form-control form-control-sm'), css_class="col-12"),
            )
        )

    class Meta:
        model = QuestionModel
        exclude = ["assessment"]

class AnswerForm(forms.Form):
    answer = forms.CharField(max_length=120)
    answer_img = forms.ImageField(help_text=_("Image for answer."), required=False)

class AnswerFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_show_labels = False
        self.form_tag = False
        self.disable_csrf = True
        self.layout = Layout(
            Row(
                Div(Field('answer', css_class='form-control form-control-sm'), css_class="col-12 col-md-6"),
                Div(Field('answer_img', css_class='form-control form-control-sm'), css_class="col-12 col-md-6"),

                # css class for the row
                css_class="answer-group",
            )
        )

AnswerFormset = forms.formset_factory(AnswerForm, extra=4)


