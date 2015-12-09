from django.contrib import admin
from .models import {{ app_name|capfirst }}

admin.site.register({{ app_name|capfirst }})
