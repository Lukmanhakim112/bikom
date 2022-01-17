from crispy_forms.layout import (
    HTML, Div, Layout, Row, Field
)



STUDENT_REGIS_FORM_LAYOUT = Layout(
    Row(
        Div(Field('username', css_class='form-control form-control-sm'), css_class='col-12'),

        Div(Field('full_name', css_class='form-control form-control-sm'), css_class='col-12 col-md-6'),
        Div(Field('phone_number', css_class='form-control form-control-sm'), css_class='col-12 col-md-6'),

        Div(Field('photo', css_class='form-control form-control-sm'), css_class='col-12'),

        Div(Field('password1', css_class='form-control form-control-sm'), css_class='col-12 col-md-6'),
        Div(Field('password2', css_class='form-control form-control-sm'), css_class='col-12 col-md-6'),

        Div(HTML('<button class="py-2 mt-3 btn btn-block btn-danger">Daftarkan Saya!</button>'), css_class='col-12 d-grid'),

        # CSS class for the row form
        css_class="p-4",
    ),
)

STUDENT_PROFILE_FORM_LAYOUT = Layout(
    Row(
        Div(Field('chield_number', css_class='form-control form-control-sm'), css_class='col-12 col-md-4'),
        Div(Field('number_of_sibling', css_class='form-control form-control-sm'), css_class='col-12 col-md-4'),
        Div(Field('klass', css_class='form-control form-control-sm'), css_class='col-12 col-md-4'),
    )
)

PARENT_STUDENT_FORM_LAYOUT = Layout(
    Row(
        Div(Field('full_name', css_class='form-control form-control-sm'), css_class='col-12 col-md-6'),
        Div(Field('jobs', css_class='form-control form-control-sm'), css_class='col-12 col-md-6'),
    )
)
