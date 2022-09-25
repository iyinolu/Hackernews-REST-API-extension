from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter(trailing_slash=True)

router.register(r'api/hnstory', views.StoryViewSet, basename="story-crud")

urlpatterns = [
    path('', include(router.urls))
]