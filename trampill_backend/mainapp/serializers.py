from rest_framework import serializers

from . import models
from django.contrib.auth import get_user_model

User = get_user_model()


class CourseItemSerializer(serializers.ModelSerializer):

    course = serializers.SlugRelatedField(queryset=models.Course.objects.all(), slug_field='name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request_user = self.context['request'].user
        self.fields['course'].queryset = models.Course.objects.filter(owner=request_user)

    class Meta:
        model = models.CourseItem
        fields = [
            "url",
            "course",
            "episode_title",
            "episode_url",
            "episode",
            "episode_note",
            "episode_archive",
            "published",
            "created",
            "last_updated",
        ]

        extra_kwargs = {
            "url": {"view_name": "api:courseitem-detail", "lookup_field": "id"}
        }


class CategorySerializer(serializers.ModelSerializer):
    course_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Category
        fields = [
            "url",
            "name",
            "course_set",
        ]
        read_only_fields = ('url', 'name', 'course_set')

        extra_kwargs = {
            "url": {"view_name": "api:category-detail", "lookup_field": "name"}
        }
        lookup_field = 'name'


class CategorySerializerNoCourseSet(CategorySerializer):

    class Meta:
        model = models.Category
        fields = [
            "url",
            "name",
        ]
        read_only_fields = ('url', 'name')

        extra_kwargs = {
            "url": {"view_name": "api:category-detail", "lookup_field": "name"}
        }


class CourseSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    url = serializers.HyperlinkedIdentityField(
        view_name='api:course-detail',
        lookup_field='name',
    )

    kategori = serializers.SlugRelatedField(queryset=models.Category.objects.all(), slug_field='name', many=True)

    class Meta:
        model = models.Course
        fields = [
            "url",
            "name",
            "user",
            "course_home",
            "kategori",
            "desc",
            "published",
            "last_updated",
            "created",
        ]
        lookup_field = 'name'


class CourseSerializerRead(CourseSerializer):
    pass
