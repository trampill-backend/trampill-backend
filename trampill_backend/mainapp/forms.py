from django import forms
from . import models


class CourseItemForm(forms.ModelForm):
    class Meta:
        model = models.CourseItem
        fields = [
            "published",
            "episode_url",
            "episode",
            "episode_note",
            "episode_title",
            "episode_archive",
            "course",
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = [
            "name",
        ]


class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = [
            "name",
            "course_home",
            "desc",
            "published",
            "user",
            "kategori",
        ]
