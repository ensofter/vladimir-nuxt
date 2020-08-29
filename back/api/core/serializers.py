from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ["id", "h1", "title", "intro", "slug", "created_data", "content"]
