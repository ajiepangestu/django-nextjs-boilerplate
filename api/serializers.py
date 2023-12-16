from django.contrib.auth.models import User, Group

from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class GroupSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'
