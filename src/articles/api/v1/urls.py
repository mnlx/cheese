from django.urls import path, include
from rest_framework import routers

from .views import ArticleViewSet


article_router = routers.SimpleRouter()
article_router.register('articles', ArticleViewSet, base_name='articles')


urlpatterns = [
    path('', include(article_router.urls))
]
