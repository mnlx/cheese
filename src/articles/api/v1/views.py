from django.utils import timezone
from rest_framework import viewsets, mixins

from articles.models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(publish_date__lt=timezone.now()).order_by('-publish_date')
