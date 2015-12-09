from django.core.urlresolvers import reverse_lazy
from django.views.generic import (ListView, CreateView,
                                  UpdateView, DeleteView)
from .forms import {{ app_name|capfirst }}Form
from .models import {{ app_name|capfirst }}


class {{ app_name|capfirst }}ListView(ListView):
    model = {{ app_name|capfirst }}


class {{ app_name|capfirst }}CreateView(CreateView):
    model = {{ app_name|capfirst }}
    form_class = {{ app_name|capfirst }}Form


class {{ app_name|capfirst }}UpdateView(UpdateView):
    model = {{ app_name|capfirst }}
    form_class = {{ app_name|capfirst }}Form


class {{ app_name|capfirst }}DeleteView(DeleteView):
    model = {{ app_name|capfirst }}
    success_url = reverse_lazy('{{ app_name }}_list')
