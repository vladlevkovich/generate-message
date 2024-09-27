from rest_framework import serializers


class UsernameSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=1)
