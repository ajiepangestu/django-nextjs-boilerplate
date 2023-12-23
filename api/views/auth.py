from api.views.base import TokenViewBase

from api.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer
)


class TokenObtainPairView(TokenViewBase):
    serializer_class = TokenObtainPairSerializer


class TokenRefreshView(TokenViewBase):
    serializer_class = TokenRefreshSerializer
