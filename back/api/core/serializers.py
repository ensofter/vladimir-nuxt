from rest_framework import serializers
from .models import Service, Tag

class ServiceSerializer(serializers.ModelSerializer):

    tag = serializers.StringRelatedField()

    class Meta:
        model = Service
        fields = ["id", "h1", "title", "intro", "slug", "created", "content", "image", "tag"]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class TagSerializer(serializers.ModelSerializer):

    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ["id", "name", "tag_slug", "services"]
        lookup_field = {
            'url': {'lookup_field': 'tag_slug'}
        }

class AsideSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ["image", "h1", "intro", "tag", "slug"]
