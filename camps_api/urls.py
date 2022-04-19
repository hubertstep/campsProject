from django.urls import path
from . import views

# api urls

app_name = 'camps_api'


urlpatterns = [
    path('employee/', views.employee_list),
    path('employee/<int:pk>', views.employee_detail)
]
