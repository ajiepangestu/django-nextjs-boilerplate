from django.contrib.auth import models

from api.views.base import ModelViewSet
from api.serializers import UserSerializer


class UserView(ModelViewSet):
    queryset = models.User.objects.all().order_by('id')
    serializer_class = UserSerializer
