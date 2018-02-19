from django.contrib.auth.models import User
from rest_framework import serializers
from posts.models import Post


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = ['first_name', 'last_name']


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
