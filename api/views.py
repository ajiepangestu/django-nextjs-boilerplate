from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet

from service.util.response import (
    send_success_response,
    send_failed_response
)
from api.serializers import GroupSerializer, UserSerializer


class BaseModelViewSet(ModelViewSet):

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return serializer.data

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return serializer.data


class UserViewSet(BaseModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        try:
            data = super().list(request, *args, **kwargs)
            result = send_success_response(data)
            return result

        except Exception as error:
            return send_failed_response(message=str(error))

    def retrieve(self, request, *args, **kwargs):
        try:
            data = super().retrieve(request, *args, **kwargs)
            return send_success_response(data)

        except Exception as error:
            return send_failed_response(message=str(error))


class GroupViewSet(BaseModelViewSet):
    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupSerializer

    def list(self, request, *args, **kwargs):
        try:
            data = super().list(request, *args, **kwargs)
            result = send_success_response(data)
            return result

        except Exception as error:
            return send_failed_response(message=str(error))

    def retrieve(self, request, *args, **kwargs):
        try:
            data = super().retrieve(request, *args, **kwargs)
            return send_success_response(data)

        except Exception as error:
            return send_failed_response(message=str(error))
