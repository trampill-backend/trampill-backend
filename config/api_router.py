from rest_framework.routers import DefaultRouter, SimpleRouter
from django.conf import settings
from trampill_backend.users.api.views import UserViewSet
from trampill_backend.mainapp import api

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

router.register("course_item", api.CourseItemViewSet)
router.register("category", api.CategoryViewSet)
router.register("course", api.CourseViewSet)


app_name = "api"
urlpatterns = router.urls
