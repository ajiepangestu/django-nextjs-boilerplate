from django.contrib.auth import models as django_models

from api.base.views import BaseModelViewSet
from api.user.serializers import UserSerializer


class UserViewSet(BaseModelViewSet):
    queryset = django_models.User.objects.all().order_by('id')
    serializer_class = UserSerializer
