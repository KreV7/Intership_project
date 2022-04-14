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


class MyUserSerializer(serializers.ModelSerializer):
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


class UserForStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
        )


class UsersStatisticSerializer(serializers.ModelSerializer):
    user = UserForStatisticSerializer()

    class Meta:
        model = AdvUser
        fields = (
            'user',
            'bought_cars',
            'spent_money',
        )
