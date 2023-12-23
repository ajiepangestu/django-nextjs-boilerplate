from django.contrib.auth import models as django_models

from api.base.views import BaseModelViewSet
from api.group.serializers import GroupSerializer


class GroupViewSet(BaseModelViewSet):
    queryset = django_models.Group.objects.all().order_by('id')
    serializer_class = GroupSerializer
