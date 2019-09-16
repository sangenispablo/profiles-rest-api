from rest_framework import serializers

class HolaSerializer(serializers.Serializer):
    """Serializer para nuestro Test HolaApiView"""
    name = serializers.CharField(max_length=10)
