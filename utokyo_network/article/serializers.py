from rest_framework import serializers
from .models import (
    Article,
    ArticleComment,
    ArticleVote
)
from user_page.serializers import UserProfileSerializer , TopicTagSerializer



class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    tags = TopicTagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'

    def get_user(self, obj):
        user = obj.user.userprofile
        serializer = UserProfileSerializer(settings.AUTH_USER_MODEL, many=False)
        return serializer.data

class ArticleCommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ArticleComment
        fields = '__all__'

    def get_user(self, obj):
        user = obj.user.userprofile
        serializer = UserProfileSerializer(settings.AUTH_USER_MODEL, many=False)
        return serializer.data

class ArticleVoteSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ArticleVote
        field = '__all__'
    
    def get_user(self, obj):
        user = obj.user.userprofile
        serializer = UserProfileSerializer(settings.AUTH_USER_MODEL, many=False)
        return serializer.data