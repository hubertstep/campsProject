from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# api urls

app_name = 'camps_api'


urlpatterns = [
    path('employee/', views.employee_list),
    path('employee/<int:pk>', views.employee_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)