from django.urls import path, include
from rest_framework import routers
from .views import ArticleViewSet, ArticleLikeListViewSet, ArticleLikeDetailsViewSet


article_router = routers.SimpleRouter()
article_router.register('articles', ArticleViewSet, base_name='articles')


urlpatterns = [
    path('', include(article_router.urls)),
    path(
        r'article/likes/<pk>/', ArticleLikeDetailsViewSet.as_view({
            'delete': 'destroy'
        }),
        name='article-details'
    ),
    path(
        r'article/likes/', ArticleLikeListViewSet.as_view({
            'get': 'list',
            'post': 'create',
        }),
        name='article-list'
    ),
]
