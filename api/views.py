from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from rest_framework.renderers import JSONRenderer
from api.models import Story
from api.serializers import StorySerializer

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
