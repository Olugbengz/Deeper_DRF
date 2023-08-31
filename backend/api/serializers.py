from rest_framework import serializers


class UserPublicSerializer(serilizers.Serializer):
    username = serializers.CharField(read_only=True)
