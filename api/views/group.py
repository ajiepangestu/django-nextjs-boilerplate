from django.contrib.auth import models

from api.views.base import ModelViewSet
from api.serializers import GroupSerializer


class GroupView(ModelViewSet):
    queryset = models.Group.objects.all().order_by('id')
    serializer_class = GroupSerializer
