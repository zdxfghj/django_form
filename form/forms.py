from .models import Artiles
from django.forms import ModelForm, TextInput,Select

class ArticleForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['first_name', 'last_name', 'email', 'service_type', 'info']


        widgets = {
            'first_name': TextInput(attrs={
                        'type': 'text',
                        "name": "first_name",
                        "placeholder" : 'First name',
                        "required": "true"
            }),
            'last_name': TextInput(attrs={
                'type': 'text',
                "name": "last_name",
                "placeholder": 'Last name',
                "required": "true"
            }),
            'email': TextInput(attrs={
                'type': 'email',
                "name": "email",
                "placeholder": 'Email',
                "required": "true"
            }),

        }