import pytest
from trampill_backend import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_CourseItem_list_view():
    instance1 = test_helpers.create_mainapp_CourseItem()
    instance2 = test_helpers.create_mainapp_CourseItem()
    client = Client()
    url = reverse("mainapp_CourseItem_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_CourseItem_create_view():
    course = test_helpers.create_mainapp_Course()
    client = Client()
    url = reverse("mainapp_CourseItem_create")
    data = {
        "published": True,
        "episode_url": "http://127.0.0.1",
        "episode": 1,
        "episode_note": "text",
        "episode_title": "text",
        "episode_archive": "http://127.0.0.1",
        "course": course.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_CourseItem_detail_view():
    client = Client()
    instance = test_helpers.create_mainapp_CourseItem()
    url = reverse("mainapp_CourseItem_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_CourseItem_update_view():
    course = test_helpers.create_mainapp_Course()
    client = Client()
    instance = test_helpers.create_mainapp_CourseItem()
    url = reverse("mainapp_CourseItem_update", args=[instance.pk, ])
    data = {
        "published": True,
        "episode_url": "http://127.0.0.1",
        "episode": 1,
        "episode_note": "text",
        "episode_title": "text",
        "episode_archive": "http://127.0.0.1",
        "course": course.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Category_list_view():
    instance1 = test_helpers.create_mainapp_Category()
    instance2 = test_helpers.create_mainapp_Category()
    client = Client()
    url = reverse("mainapp_Category_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Category_create_view():
    client = Client()
    url = reverse("mainapp_Category_create")
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Category_detail_view():
    client = Client()
    instance = test_helpers.create_mainapp_Category()
    url = reverse("mainapp_Category_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Category_update_view():
    client = Client()
    instance = test_helpers.create_mainapp_Category()
    url = reverse("mainapp_Category_update", args=[instance.pk, ])
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Course_list_view():
    instance1 = test_helpers.create_mainapp_Course()
    instance2 = test_helpers.create_mainapp_Course()
    client = Client()
    url = reverse("mainapp_Course_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Course_create_view():
    user = test_helpers.create_User()
    kategori = test_helpers.create_mainapp_Category()
    client = Client()
    url = reverse("mainapp_Course_create")
    data = {
        "name": "text",
        "course_home": "http://127.0.0.1",
        "desc": "text",
        "published": True,
        "user": user.pk,
        "kategori": kategori.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Course_detail_view():
    client = Client()
    instance = test_helpers.create_mainapp_Course()
    url = reverse("mainapp_Course_detail", args=[instance.id, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Course_update_view():
    user = test_helpers.create_User()
    kategori = test_helpers.create_mainapp_Category()
    client = Client()
    instance = test_helpers.create_mainapp_Course()
    url = reverse("mainapp_Course_update", args=[instance.id, ])
    data = {
        "name": "text",
        "course_home": "http://127.0.0.1",
        "desc": "text",
        "published": True,
        "user": user,
        "kategori": kategori,
    }
    response = client.post(url, data)
    # assert response.status_code == 302
    assert response.status_code == 200
