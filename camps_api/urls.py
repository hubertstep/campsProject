from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# api urls

app_name = 'camps_api'


urlpatterns = [
    path('employee/', views.EmployeeList.as_view(), name='employeelist'),
    path('employee/<int:pk>', views.EmployeeDetail.as_view(), name='employeedetail'),
    path('parent/', views.ParentList.as_view(), name='parentlist'),
    path('parent/<int:pk>', views.ParentDetail.as_view(), name='parentdetail'),
    path('group/', views.GroupList.as_view(), name='grouplist'),
    path('group/<int:pk>', views.GroupDetail.as_view(), name='groupdetail'),
    path('activity/', views.ActivityList.as_view(), name='activitylist'),
    path('activity/<int:pk>', views.ActivityDetail.as_view(), name='activitydetail'),
    path('participant/', views.ParticipantList.as_view(), name='participantlist'),
    path('participant/<int:pk>', views.ParticipantDetail.as_view(), name='participantdetail'),
    path('program_activity/', views.ProgramActivityList.as_view(), name='program_activitylist'),
    path('program_activity/<int:pk>', views.ProgramActivityDetail.as_view(), name='programactivitydetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)