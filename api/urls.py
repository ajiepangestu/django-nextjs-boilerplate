from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenRefreshView
)

from api.user.views import UserView
from api.group.views import GroupView
from api.auth.views import TokenObtainPairView

router = routers.DefaultRouter()
router.register('user', UserView)
router.register('group', GroupView)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]
