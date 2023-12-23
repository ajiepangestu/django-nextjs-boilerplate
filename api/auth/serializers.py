from typing import Any, Dict

from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as JWTTokenObtainPairSerializer
)
from rest_framework_simplejwt.settings import api_settings


class TokenObtainPairSerializer(JWTTokenObtainPairSerializer):

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["expired"] = refresh.payload.get('exp')

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
