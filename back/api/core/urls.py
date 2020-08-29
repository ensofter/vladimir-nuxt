from django.urls import path, include
from .views import ServiceView, ServiceDetailView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("services/", ServiceView.as_view()),
    path("services/<slug:slug>/", ServiceDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
