
from django.contrib.auth import models as django_models

from rest_framework.serializers import ModelSerializer


class GroupSerializer(ModelSerializer):

    class Meta:
        model = django_models.Group
        fields = '__all__'
