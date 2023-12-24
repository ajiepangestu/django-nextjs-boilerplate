from typing import Any, Dict

from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as JWTTokenObtainPairSerializer,
    TokenRefreshSerializer as JWTTokenRefreshSerializer,
)
from rest_framework_simplejwt.settings import api_settings


class TokenObtainPairSerializer(JWTTokenObtainPairSerializer):

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['expired'] = refresh.payload.get('exp')

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class TokenRefreshSerializer(JWTTokenRefreshSerializer):

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        refresh = self.token_class(attrs['refresh'])

        data = {'access': str(refresh.access_token)}

        if api_settings.ROTATE_REFRESH_TOKENS:
            if api_settings.BLACKLIST_AFTER_ROTATION:
                try:
                    # Attempt to blacklist the given refresh token
                    refresh.blacklist()
                except AttributeError:
                    # If blacklist app not installed, `blacklist` method will
                    # not be present
                    pass

            refresh.set_jti()
            refresh.set_exp()
            refresh.set_iat()

            data['refresh'] = str(refresh)
            data['expired'] = refresh.payload.get('exp')

        return data
