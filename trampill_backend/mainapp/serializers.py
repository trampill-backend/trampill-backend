from rest_framework import serializers

from . import models


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
            "name",
            "created",
            "last_updated",
        ]

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = [
            "name",
            "course_home",
            "kategori",
            "desc",
            "published",
            "last_updated",
            "created",
        ]
