from django.conf.urls import url
from .views import {{ app_name|capfirst }}ListView, {{ app_name|capfirst }}CreateView, {{ app_name|capfirst }}UpdateView, {{ app_name|capfirst }}DeleteView

urlpatterns = [
    url(r'^$', {{ app_name|capfirst }}ListView.as_view(), name='{{ app_name }}_list'),
    url(r'add/$', {{ app_name|capfirst }}CreateView.as_view(), name='{{ app_name }}_add'),
    url(r'(?P<pk>[0-9]+)/$', {{ app_name|capfirst }}UpdateView.as_view(), name='{{ app_name }}_update'),
    url(r'(?P<pk>[0-9]+)/delete/$', {{ app_name|capfirst }}DeleteView.as_view(), name='{{ app_name }}_delete'),
]
