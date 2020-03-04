from rest_framework import serializers

from . import models
from django.contrib.auth import get_user_model

User = get_user_model()


class CourseItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CourseItem
        fields = [
            "episode_title",
            "episode_url",
            "episode",
            "episode_note",
            "episode_archive",
            "published",
            "created",
            "last_updated",
        ]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = [
            "id",
            "name",
        ]


class CourseSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Course
        fields = [
            "name",
            "user",
            "course_home",
            "kategori",
            "desc",
            "published",
            "last_updated",
            "created",
        ]
