from rest_framework import serializers

from . import models


class CourseItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CourseItem
        fields = [
            "last_updated",
            "published",
            "episode_url",
            "created",
            "episode",
            "episode_note",
            "episode_title",
            "episode_archive",
        ]

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = [
            "created",
            "name",
            "last_updated",
        ]

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = [
            "last_updated",
            "name",
            "created",
            "course_home",
            "desc",
            "published",
        ]
