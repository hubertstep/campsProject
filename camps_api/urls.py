from django.urls import path, include
from rest_framework import routers
from . import views

# api urls

app_name = 'camps_api'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
