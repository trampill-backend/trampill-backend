from django.conf import settings
from django.conf.urls import url
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


urlpatterns = [
    path("", include("trampill_backend.mainapp.urls")),
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("trampill_backend.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# API URLS

public_apis = [
    # API base url
    path('api/v1/auth/', include('rest_framework.urls'), ),

    # apps apis
    path("api/v1/", include("config.api_router", namespace='apis_docs')),

    # DRF auth token
    path("api/v1/auth-token/", obtain_auth_token),

    # JWT
    path('api/v1/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]

schema_view = get_schema_view(
   openapi.Info(
      title="Trampill BACKEND API",
      default_version='v1',
      description="Documentation of trampill apps backend",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="root@trampill.com"),
      license=openapi.License(name="MIT License"),
   ),
   patterns=public_apis,
   public=True,
   permission_classes=(permissions.AllowAny,),
)

swagger_url = [
   url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# schema_view = get_swagger_view(title="Trampill Backend API", patterns=public_apis)

internal_apis = [
    path('api/docs/', schema_view, name='swaggerurl'),
]

urlpatterns += swagger_url + public_apis + internal_apis

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
