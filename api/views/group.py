from django.contrib.auth import models as django_models

from api.views.base import ModelViewSet
from api.serializers import GroupSerializer


class GroupView(ModelViewSet):
    queryset = django_models.Group.objects.all().order_by('id')
    serializer_class = GroupSerializer
