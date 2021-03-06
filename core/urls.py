"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.authtoken import views
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter

from to_do.urls import router as to_do_router
from bucket.urls import router as bucket_router
from core.views import UserViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Platform APIs",
      default_version='v1',
      description="Fractal Analytics Fullstack Assignment Django APIs",
   ),
   public=True,
   permission_classes=(AllowAny,),
)

core_router = DefaultRouter()
core_router.register(r'user', UserViewSet)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/user/token/', views.obtain_auth_token, name='user-token'),
    url(r'^api/', include(core_router.urls)),
    url(r'^api/', include(bucket_router.urls)),
    url(r'^api/', include(to_do_router.urls)),
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
