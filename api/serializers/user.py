
from django.contrib.auth import models as django_models
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):

    class Meta:
        model = django_models.User
        fields = [
            'id', 'first_name', 'last_name',
            'username', 'email', 'is_active',
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['group'] = instance.groups.all().values_list(
            'name',
            flat=True
        )
        return data
