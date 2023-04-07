from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
from .models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
            model = User
            fields = (
                'id', 'username', 'email', 'password'
            )

            extra_kwargs = {
                    'username': {
                    'required': True
                },
                'email': {
                    'required': True
                },
                'password': {
                    'write_only': True,
                    'required': True
                }
            }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = '__all__'
