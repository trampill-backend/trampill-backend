from django.contrib import admin
from django import forms

from . import models


class CourseItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.CourseItem
        fields = "__all__"


class CourseItemAdmin(admin.ModelAdmin):
    form = CourseItemAdminForm
    list_display = [
        "last_updated",
        "published",
        "episode_url",
        "created",
        "episode",
        "episode_note",
        "episode_title",
        "episode_archive",
    ]
    readonly_fields = [
        "last_updated",
        "published",
        "episode_url",
        "created",
        "episode",
        "episode_note",
        "episode_title",
        "episode_archive",
    ]


class CategoryAdminForm(forms.ModelForm):

    class Meta:
        model = models.Category
        fields = "__all__"


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = [
        "created",
        "name",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "name",
        "last_updated",
    ]


class CourseAdminForm(forms.ModelForm):

    class Meta:
        model = models.Course
        fields = "__all__"


class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm
    list_display = [
        "last_updated",
        "name",
        "created",
        "course_home",
        "desc",
        "published",
    ]
    readonly_fields = [
        "last_updated",
        "name",
        "created",
        "course_home",
        "desc",
        "published",
    ]


admin.site.register(models.CourseItem, CourseItemAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Course, CourseAdmin)
