from django.contrib.auth.models import User
from rest_framework import serializers

from mainapp.models import AdvUser


class AdvUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvUser
        fields = (
            'phone',
            'cash_balance'
        )


class UserSerializer(serializers.ModelSerializer):
    advuser = AdvUserSerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'advuser'
        )
