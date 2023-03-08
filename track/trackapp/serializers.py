from rest_framework import serializers

from .models import Loc

class LocSerializer(serializers.Serializer):
    latitude = serializers.CharField(max_length=120)
    longitude = serializers.CharField(max_length=120)
    def create(self, validated_data):
        return Loc.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.save()
        return instance

