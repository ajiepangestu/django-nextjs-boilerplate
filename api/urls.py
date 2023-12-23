from django.urls import include, path
from rest_framework import routers

from api.views import (
    TokenObtainPairView,
    TokenRefreshView,
    UserView,
    GroupView
)

router = routers.DefaultRouter()
router.register('user', UserView)
router.register('group', GroupView)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
