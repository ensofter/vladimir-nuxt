from django.shortcuts import render
from .serializers import ServiceSerializer
from .models import Service
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

class ServiceView(APIView):
    """
    List of all Services
    """
    def get(self, request, format=None):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

class ServiceDetailView(APIView):

    def get_object(self, slug):
        try:
            return Service.objects.get(slug=slug)
        except Service.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        service = self.get_object(slug)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)
