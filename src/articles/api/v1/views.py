from django.utils import timezone
from rest_framework import viewsets, mixins

from articles.models import Article, ArticleLikes
from rest_framework.pagination import LimitOffsetPagination

from .serializers import ArticleSerializer, ArticleLikesSerializer


class ArticleViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
    Return a list of all published articles ordered by date.
    """
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(created__lt=timezone.now()).order_by('-publish_date')


class ArticleLikesDetailsViewSet(viewsets.ModelViewSet):
    """
    hero:

    """
    serializer_class = ArticleLikesSerializer

    def get_queryset(self):
        return ArticleLikes.objects.all()

class ArticleLikesListViewSet(viewsets.ModelViewSet):
    """
    hero:

    """
    serializer_class = ArticleLikesSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        query_params = self.request.query_params
        user= 'user' in  query_params and query_params['user']
        article = 'article' in query_params and query_params['article']
        if user and article :
            return ArticleLikes.objects.filter(user__pk=user).filter(article__pk=article)
        elif user :
            return ArticleLikes.objects.filter(article__pk=article)
        elif article:
            return ArticleLikes.objects.filter(user__pk=user)
        else:
            return ArticleLikes.objects.all()



