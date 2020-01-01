from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from animals.models import Cat, Dog


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cat
        fields = '__all__'

    def validate(self, data):
        owner = data.get('owner')
        user = self.context['request'].user
        if owner and not user == owner:
            raise PermissionDenied()
        return data


class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = '__all__'

    def validate(self, data):
        owner = data.get('owner')
        user = self.context['request'].user
        if owner and not user == owner:
            raise PermissionDenied()
        return data
