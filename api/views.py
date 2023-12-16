from django.contrib.auth import models as django_models
from rest_framework.viewsets import ModelViewSet

from service.util.response import (
    send_success_response,
    send_failed_response
)
from api.serializers import GroupSerializer, UserSerializer


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
                return send_failed_response(message='Not Found')

            return send_success_response(data)

        except Exception as error:
            status = 500
            if 'the given query' in str(error):
                status = 404

            return send_failed_response(
                status=status,
                message=str(error)
            )

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            data = serializer.data
            if not data:
                return send_failed_response(message='Not Found')

            return send_success_response(data)

        except Exception as error:
            status = 500
            if 'the given query' in str(error):
                status = 404

            return send_failed_response(
                status=status,
                message=str(error)
            )


class UserViewSet(BaseModelViewSet):
    queryset = django_models.User.objects.all().order_by('id')
    serializer_class = UserSerializer


class GroupViewSet(BaseModelViewSet):
    queryset = django_models.Group.objects.all().order_by('id')
    serializer_class = GroupSerializer
