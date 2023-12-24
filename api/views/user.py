from django.contrib.auth import models as django_models

from api.views.base import ModelViewSet
from api.serializers import UserSerializer


class UserView(ModelViewSet):
    queryset = django_models.User.objects.all().order_by('id')
    serializer_class = UserSerializer
