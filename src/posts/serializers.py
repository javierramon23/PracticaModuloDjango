from rest_framework import serializers
from posts.models import Post
from users.serializers import UserSerializer


class PostAddSerializer(serializers.ModelSerializer):

    owner = UserSerializer(read_only=True)

    class Meta:
        model = Post
        exclude = ['create_at', 'id']


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'url', 'summary', 'publish_date']


class PostDetailSerializer(serializers.ModelSerializer):

    owner = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
