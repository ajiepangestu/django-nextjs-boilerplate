from rest_framework.viewsets import ModelViewSet

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.views import (
    TokenViewBase as JWTTokenViewBase
)
from rest_framework_simplejwt.exceptions import TokenError

from api.utils import response


class BaseModelViewSet(ModelViewSet):

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                data = self.get_paginated_response(serializer.data)

            else:
                serializer = self.get_serializer(queryset, many=True)
                data = serializer.data

            if not data:
                return response(status=404, message='Not Found')

            return response(data=data)

        except Exception as error:
            status = 500
            if 'the given query' in str(error):
                status = 404

            return response(
                status=status,
                message=str(error)
            )

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            data = serializer.data
            if not data:
                return response(
                    status=404,
                    message='Not Found'
                )

            return response(data=data)

        except Exception as error:
            status = 500
            if 'the given query' in str(error):
                status = 404

            return response(
                status=status,
                message=str(error)
            )


class TokenViewBase(JWTTokenViewBase):
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)

        except TokenError as e:
            return response(
                status=401,
                message=e.args[0]
            )

        except AuthenticationFailed as e:
            return response(
                status=401,
                message=str(e)
            )

        return response(data=serializer.validated_data)
