from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import TodoText
from django.contrib.auth.models import User


class TodoTextSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=TodoText.objects.all())]
    )

    class Meta:
        model = TodoText
        fields = ('id',
                  'username',
                  'email',
                  'text',
                  'status',)


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    ),
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  )
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
        }


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  )
        extra_kwargs = {
            'password': {'write_only': True},
        }
