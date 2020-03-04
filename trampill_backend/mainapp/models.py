from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class CourseItem(models.Model):

    #  Relationships
    course = models.ForeignKey("Course", on_delete=models.CASCADE)

    #  Fields
    published = models.BooleanField(default=True)
    episode_url = models.URLField()

    episode = models.PositiveSmallIntegerField()
    episode_note = models.TextField()
    episode_title = models.CharField(max_length=80)
    episode_archive = models.URLField(
        help_text="please use dropbox or anything similar to attach your files, and hook the url to this field"
    )

    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("mainapp_CourseItem_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("mainapp_CourseItem_update", args=(self.pk,))


class Category(models.Model):

    #  Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=80)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("mainapp_Category_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("mainapp_Category_update", args=(self.pk,))


class Course(models.Model):

    #  Relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kategori = models.ManyToManyField("Category")

    #  Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    course_home = models.URLField()
    desc = models.TextField()
    published = models.BooleanField(default=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("mainapp_Course_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("mainapp_Course_update", args=(self.pk,))

