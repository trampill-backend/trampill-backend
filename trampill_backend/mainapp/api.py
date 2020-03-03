from rest_framework import viewsets, permissions

from . import serializers
from . import models


class CourseItemViewSet(viewsets.ModelViewSet):
    """ViewSet for the CourseItem class"""

    queryset = models.CourseItem.objects.all()
    serializer_class = serializers.CourseItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the Category class"""

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet for the Course class"""

    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
