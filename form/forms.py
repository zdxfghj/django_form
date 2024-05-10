from .models import FeedBack
from django.forms import ModelForm, TextInput, Select, CheckboxInput


class ArticleForm(ModelForm):
    class Meta:
        model = FeedBack
        fields = '__all__'
        # fields = ['first_name', 'last_name', 'email', 'service_type', 'info', '']

        widgets = {
            'first_name': TextInput(attrs={
                'type': 'text',
                "name": "first_name",
                "placeholder": 'First name',
                "required": "true",
                'class': 'form-control'
            }),
            'last_name': TextInput(attrs={
                'type': 'text',
                "name": "last_name",
                "placeholder": 'Last name',
                "required": "true",
                'class': 'form-control'
            }),
            'email': TextInput(attrs={
                'type': 'email',
                "name": "email",
                "placeholder": 'Email',
                "required": "true",
                'class': 'form-control'
            }),
            "personalize_ads": CheckboxInput(attrs={
                'type': 'checkbox',
                'class': 'form-check-input'
            }),
            'mark_communication': CheckboxInput(attrs={
                'type': 'checkbox',
                'class': 'form-check-input'
            })

        }
