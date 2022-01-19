from django.urls import path, re_path, include
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'users', UserViewSet)


urlpatterns = [
    re_path(r'api/', include(router.urls)),
]