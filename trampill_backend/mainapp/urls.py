from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("CourseItem", api.CourseItemViewSet)
router.register("Category", api.CategoryViewSet)
router.register("Course", api.CourseViewSet)

urlpatterns = (
    # path("api/v1/", include(router.urls)),
    path("mainapp/course_item/", views.CourseItemListView.as_view(), name="mainapp_CourseItem_list"),
    path("mainapp/course_item/create/", views.CourseItemCreateView.as_view(), name="mainapp_CourseItem_create"),
    path("mainapp/course_item/detail/<int:pk>/", views.CourseItemDetailView.as_view(), name="mainapp_CourseItem_detail"),
    path("mainapp/course_item/update/<int:pk>/", views.CourseItemUpdateView.as_view(), name="mainapp_CourseItem_update"),
    path("mainapp/category/", views.CategoryListView.as_view(), name="mainapp_Category_list"),
    path("mainapp/category/create/", views.CategoryCreateView.as_view(), name="mainapp_Category_create"),
    path("mainapp/category/detail/<int:pk>/", views.CategoryDetailView.as_view(), name="mainapp_Category_detail"),
    path("mainapp/category/update/<int:pk>/", views.CategoryUpdateView.as_view(), name="mainapp_Category_update"),
    path("mainapp/course/", views.CourseListView.as_view(), name="mainapp_Course_list"),
    path("mainapp/course/create/", views.CourseCreateView.as_view(), name="mainapp_Course_create"),
    path("mainapp/course/detail/<int:pk>/", views.CourseDetailView.as_view(), name="mainapp_Course_detail"),
    path("mainapp/course/update/<int:pk>/", views.CourseUpdateView.as_view(), name="mainapp_Course_update"),
)
