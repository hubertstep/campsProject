from django.urls import path
from django.views.generic import TemplateView
# camps urls

app_name = 'camps'

urlpatterns = [
    path('', TemplateView.as_view(template_name='camps/index.html')),
]
