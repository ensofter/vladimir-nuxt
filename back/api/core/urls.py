from django.urls import path, include
from .views import ServiceView, ServiceDetailView, TagView, TagDetailView, AsideView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("services/", ServiceView.as_view()),
    path("services/<slug:slug>/", ServiceDetailView.as_view()),
    path("tag/", TagView.as_view()),
    path("tag/<slug:tag_slug>/", TagDetailView.as_view()),
    path("aside/", AsideView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
