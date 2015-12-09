from django.core.urlresolvers import reverse
from django.db import models


class {{ app_name|capfirst }}(models.Model):
    def get_absolute_url(self):
        return reverse('{{ app_name }}_list')
