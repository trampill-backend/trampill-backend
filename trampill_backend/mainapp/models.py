from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class CourseItem(models.Model):

    #  Relationships
    course = models.ForeignKey("Course", on_delete=models.CASCADE)

    #  Fields
    published = models.BooleanField(default=True)
    episode_url = models.URLField(
        null=True,
        blank=True,
        help_text=_("You can use YouTube URL Here..")
    )

    episode = models.PositiveSmallIntegerField()
    episode_note = models.TextField(
        help_text=_("Note for this episode..")
    )
    episode_title = models.CharField(max_length=200)
    episode_archive = models.URLField(
        null=True,
        blank=True,
        help_text=_("Please use dropbox or anything similar to attach your files, and hook the url to this field")
    )

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("mainapp_CourseItem_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("mainapp_CourseItem_update", args=(self.pk,))

    @cached_property
    def owner(self):
        return self.course.owner


class Category(models.Model):

    #  Fields
    name = models.CharField(max_length=150, unique=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("mainapp_Category_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("mainapp_Category_update", args=(self.pk,))


class Course(models.Model):

    #  Relationships
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    kategori = models.ManyToManyField("Category")

    #  Fields
    name = models.CharField(max_length=300, unique=True)
    course_home = models.URLField(
        null=True,
        blank=True,
        help_text=_("External URL about the course paste here")
    )
    desc = models.TextField(
        help_text=_("Make a description of your course is mandatory! :)")
    )
    published = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("mainapp_Course_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("mainapp_Course_update", args=(self.pk,))

