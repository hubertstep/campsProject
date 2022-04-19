from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# api urls

app_name = 'camps_api'


urlpatterns = [
    path('employee/', views.EmployeeList.as_view()),
    path('employee/<int:pk>', views.EmployeeDetail.as_view()),
    path('parent/', views.ParentList.as_view()),
    path('parent/<int:pk>', views.ParentDetail.as_view()),
    path('group/', views.GroupList.as_view()),
    path('group/<int:pk>', views.GroupDetail.as_view()),
    path('activity/', views.ActivityList.as_view()),
    path('activity/<int:pk>', views.ActivityDetail.as_view()),
    path('participant/', views.ParticipantList.as_view()),
    path('participant/<int:pk>', views.ParticipantDetail.as_view()),
    path('program_activity/', views.ProgramActivityList.as_view()),
    path('program_activity/<int:pk>', views.ProgramActivityDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)