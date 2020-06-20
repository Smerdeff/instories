from crispy_forms.bootstrap import FormActions
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, Div, Field
from django.forms import DateField

from .models import Pushes


class DateInput(forms.DateInput):
    input_type = 'date'


class PushesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PushesForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Div(
                    Div(
                        Field('title', css_class='form-control', placeholder='Укажите заголовок'),
                        Field('text', css_class='form-control', placeholder='Введите текст уведомления'),
                        Field('sent_at', css_class='form-control', ),
                        css_class='col-lg-6 col-md-6 col-sm-12'),
                    Div(
                        template='admin/pushes/preview.html',
                        css_class='col-lg-6 col-md-6 col-sm-12'),
                    css_class='row'
                )
                # ,  css_class='container'
            )
        )
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Отправить'))

    class Meta:
        model = Pushes
        fields = ['title', 'text', 'sent_at']
        widgets = {'sent_at': DateInput()}
