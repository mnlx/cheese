from django.urls import path, include
from rest_framework import routers
from .views import ArticleViewSet, ArticleLikesListViewSet


article_router = routers.SimpleRouter()
article_router.register('articles', ArticleViewSet, base_name='articles')


urlpatterns = [
    path('', include(article_router.urls)),
    path(
        r'article/likes/', ArticleLikesListViewSet.as_view({
            'get': 'list',
            'post': 'create',
            'delete': 'destroy'

        }),
        name='article-list'
    ),
]
