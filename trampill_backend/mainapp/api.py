from django.core.cache import cache
from rest_framework import viewsets, permissions
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response

from . import serializers, serializers_fast
from . import models
from .permission import IsOwnerOrReadOnly


class CourseItemViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return the given Course Item.

    list:
        Return a list of all Course Item.

    create:
        Create a new Course Item.

    destroy:
        Delete a Course Item.

    update:
        Update a Course Item.

    partial_update:
        Update a Course Item.
    """

    queryset = models.CourseItem.objects.all()
    serializer_class = serializers.CourseItemSerializer
    # serializer_class = serializers_fast.course_item_serializer()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'id'

    def get_queryset(self):
        return models.CourseItem.objects.filter(course__owner=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return the given Category.

    list:
        Return a list of all Category.

    create:
        Create a new Category.

    destroy:
        Delete a Category.

    update:
        Update a Category.

    partial_update:
        Update a Category.
    """
    qs = cache.get_or_set('category_all', models.Category.objects.all())
    queryset = qs
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'name'


class CourseViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return the given Course.

    list:
        Return a list of all Course.

    create:
        Create a new Course.

    destroy:
        Delete a Course.

    update:
        Update a Course.

    partial_update:
        Update a Course.
    """

    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'name'

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.CourseSerializerRead
        return self.serializer_class

    def update(self, request, *args, **kwargs):
        pass
