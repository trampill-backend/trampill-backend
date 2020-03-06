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
        "course",
        "episode",
        "episode_title",
        "episode_note",
        "episode_archive",
        "episode_url",
        "published",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class CategoryAdminForm(forms.ModelForm):

    class Meta:
        model = models.Category
        fields = "__all__"


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = [
        "name",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class CourseAdminForm(forms.ModelForm):

    class Meta:
        model = models.Course
        fields = "__all__"


class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm
    list_display = [
        "name",
        "course_home",
        "desc",
        "published",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


admin.site.register(models.CourseItem, CourseItemAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Course, CourseAdmin)
