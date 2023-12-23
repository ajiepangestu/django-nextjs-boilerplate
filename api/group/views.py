from django.contrib.auth import models as django_models

from api.base.views import BaseModelViewSet
from api.group.serializers import GroupSerializer


class GroupView(BaseModelViewSet):
    queryset = django_models.Group.objects.all().order_by('id')
    serializer_class = GroupSerializer
