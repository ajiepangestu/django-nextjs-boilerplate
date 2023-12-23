from rest_framework.viewsets import ModelViewSet

from api.util.response import (
    success,
    failed
)


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
                return failed(message='Not Found')

            return success(data)

        except Exception as error:
            status = 500
            if 'the given query' in str(error):
                status = 404

            return failed(
                status=status,
                message=str(error)
            )

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            data = serializer.data
            if not data:
                return failed(message='Not Found')

            return success(data)

        except Exception as error:
            status = 500
            if 'the given query' in str(error):
                status = 404

            return failed(
                status=status,
                message=str(error)
            )
