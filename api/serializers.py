from django.contrib.auth.models import User, Group

from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
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


class GroupSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'
