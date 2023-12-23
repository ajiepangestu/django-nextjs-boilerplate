from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenRefreshView
)

from api.user.views import UserViewSet
from api.group.views import GroupViewSet
from api.auth.views import TokenObtainPairView

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('group', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]
