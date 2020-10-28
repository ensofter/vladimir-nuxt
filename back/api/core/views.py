from django.shortcuts import render
from .serializers import ServiceSerializer, TagSerializer, AsideSerializer
from .models import Service, Tag
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import generics
from rest_framework import pagination

class PageNumberSetPagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    ordering = 'created'

class ServiceView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = PageNumberSetPagination

class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'slug'

class TagView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetailView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    pagination_class = PageNumberSetPagination

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        return Service.objects.filter(tag__tag_slug=tag_slug)

class AsideView(generics.ListAPIView):
    queryset = Service.objects.all().order_by('-id')[:6]
    serializer_class = AsideSerializer
