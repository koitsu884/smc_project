from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div

from .models import Car


class CarSearchForm(forms.Form):
    fields = [
        'price',
        'model', 
        'body_type', 
        'transmission',
    ]

    def __init__(self, *args, **kwargs):
        super(CarSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                Div(
                    'price',
                    css_id='form-control'
                ),
                'model',
                'body_type',
                'transmission',
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )

