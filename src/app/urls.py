"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from articles import urls as articles_urls


schema_view = get_schema_view(
   openapi.Info(
      title="CKL News API",
      default_version='v1',
   ),
   public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(articles_urls)),

    path('api/docs/', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),
]


if settings.DEBUG:
    urlpatterns += [
        re_path(r'^{}(?P<path>.*)$'.format(settings.MEDIA_URL), serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
