from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from api.models import Story, Comments

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ["id", "text"]


class StorySerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Story
        fields = ["id", "title", "text", "comments"]