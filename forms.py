from django.forms import ModelForm
from .models import {{ app_name|capfirst }}


class {{ app_name|capfirst }}Form(ModelForm):
    class Meta:
        model = {{ app_name|capfirst }}
