from crispy_forms.layout import (
    Layout, Div, Row, Field
)


TEACHER_CREATION_FORM_LAYOUT = Layout(
    Row(
        Div(Field('username', css_class='form-control form-control-sm'), css_class='col-12 col-md-6'),
        Div(Field('full_name', css_class='form-control form-control-sm'), css_class='col-12 col-md-6'),

        Div(Field('phone_number', css_class='form-control form-control-sm'), css_class='col-12'),
        Div(Field('photo', css_class='form-control form-control-sm'), css_class='col-12'),

        Div(Field('password1', css_class='form-control form-control-sm'), css_class='col-12 col-md-6'),
        Div(Field('password2', css_class='form-control form-control-sm'), css_class='col-12 col-md-6'),
        Div('is_staff', css_class='col-12'),
    )
)
