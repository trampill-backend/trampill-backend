from rest_framework import viewsets, permissions

from . import serializers, serializers_fast
from . import models


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
    permission_classes = [permissions.IsAuthenticated]


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

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


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
    permission_classes = [permissions.IsAuthenticated]
