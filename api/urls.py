from django.urls import include, path
from rest_framework import routers

from api.views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('group', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
