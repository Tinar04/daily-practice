from rest_framework import serializers

class ShortenSerializer(serializers.Serializer):
    original_url = serializers.URLField()