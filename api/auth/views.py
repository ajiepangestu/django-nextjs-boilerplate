
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.views import (
    TokenObtainPairView as JWTTokenObtainPairView
)
from rest_framework_simplejwt.exceptions import TokenError

from api.auth.serializers import TokenObtainPairSerializer
from api.util.response import failed, success


class TokenObtainPairView(JWTTokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)

        except TokenError as e:
            return failed(data=e.args[0], status=401)

        except AuthenticationFailed as e:
            return failed(status=401, message=str(e))

        return success(data=serializer.validated_data)
