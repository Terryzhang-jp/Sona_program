from rest_framework import serializers
from django.contrib.auth.models import User
from django.conf import settings

from .models import Mumble
from user_page.serializers import UserProfileSerializer, UserSerializer


class MumbleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    original_mumble = serializers.SerializerMethodField(read_only=True)
    up_voters = serializers.SerializerMethodField(read_only=True)
    down_voters = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Mumble
        fields = '__all__'

    def get_user(self, obj):
        user_profile = obj.user.userprofile
        serializer = UserProfileSerializer(user_profile, many=False)
        return serializer.data


    def get_original_mumble(self, obj):
        original = obj.remumble
        if original != None:
            serializer = MumbleSerializer(original, many=False)
            return serializer.data
        else:
            return None

    def get_up_voters(self, obj):
        # Returns list of users that upvoted post
        voters = obj.votes.through.objects.filter(mumble=obj, value='upvote').values_list('user', flat=True)

        voter_objects = obj.votes.filter(id__in=voters)
        serializer = UserSerializer(voter_objects, many=True)
        return serializer.data

    def get_down_voters(self, obj):
        # Returns list of users that upvoted post
        voters = obj.votes.through.objects.filter(mumble=obj, value='downvote').values_list('user', flat=True)

        voter_objects = obj.votes.filter(id__in=voters)
        serializer = UserSerializer(voter_objects, many=True)
        return serializer.data