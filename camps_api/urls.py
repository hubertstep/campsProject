from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# api urls

app_name = 'camps_api'


urlpatterns = [
    path('employee/', views.EmployeeList.as_view()),
    path('employee/<int:pk>', views.EmployeeDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)