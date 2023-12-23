from api.base.views import TokenViewBase

from api.auth.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer
)


class TokenObtainPairView(TokenViewBase):
    serializer_class = TokenObtainPairSerializer


class TokenRefreshView(TokenViewBase):
    serializer_class = TokenRefreshSerializer
