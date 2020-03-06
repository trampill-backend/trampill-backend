import random
import string

# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

from trampill_backend.mainapp import models as mainapp_models
User = get_user_model()


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_mainapp_CourseItem(**kwargs):
    defaults = {}
    defaults["published"] = True
    defaults["episode_url"] = ""
    defaults["episode"] = 2
    defaults["episode_note"] = ""
    defaults["episode_title"] = ""
    defaults["episode_archive"] = ""
    if "course" not in kwargs:
        defaults["course"] = create_mainapp_Course()
    defaults.update(**kwargs)
    return mainapp_models.CourseItem.objects.create(**defaults)

def create_mainapp_Category(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults.update(**kwargs)
    return mainapp_models.Category.objects.create(**defaults)

def create_mainapp_Course(**kwargs):
    defaults = {}
    defaults["name"] = "test course"
    defaults["course_home"] = ""
    defaults["desc"] = ""
    defaults["published"] = True
    if "user" not in kwargs:
        defaults["owner"] = create_User()

    defaults.update(**kwargs)
    instance = mainapp_models.Course.objects.create(**defaults)

    if "kategori" not in kwargs:
        defaults["kategori"] = (create_mainapp_Category(), create_mainapp_Category())
    defaults.update(**kwargs)

    # return mainapp_models.Course.objects.create(**defaults)
    instance.kategori.set(defaults["kategori"])
    instance.save()
    return instance
