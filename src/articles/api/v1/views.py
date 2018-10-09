from rest_framework import viewsets, mixins
from articles.models import Article, ArticleLike
from rest_framework.pagination import LimitOffsetPagination
from .serializers import ArticleSerializer, ArticleLikesSerializer
from django.utils import timezone


class ArticleViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
    Return a list of all published articles ordered by date.
    When query ?filter=homepage, returns the top five rated articles
    in order of likes, plus the rest ordered by publishing date
    """
    serializer_class = ArticleSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        query_params = self.request.query_params
        filter = 'filter' in query_params and query_params['filter']
        if filter == 'homepage':
            query = '''
                    SELECT  * FROM articles_article a
                    LEFT JOIN (
                        SELECT article_id, COUNT(*) as likes
                        FROM articles_articlelike
                        WHERE created > NOW() - INTERVAL '72' HOUR
                        GROUP BY article_id ) likes ON likes.article_id=a.id
                    ORDER BY likes IS NOT NULL DESC, likes DESC, publish_date DESC
                    '''
            return list(Article.objects.raw(query))
        else:
            return Article.objects.filter(created__lt=timezone.now()).order_by('-publish_date')

class ArticleLikeDetailsViewSet(viewsets.ModelViewSet):
    """
    details:
    Returns the specific ArticleLikes model according to the id in the URI
    """
    serializer_class = ArticleLikesSerializer
    queryset = ArticleLike.objects.all()

class ArticleLikeListViewSet(viewsets.ModelViewSet):
    """
    list:
    Returns a list of the ArticleLikes model filtered by URI queries
    """
    serializer_class = ArticleLikesSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        query_params = self.request.query_params
        user = 'user' in query_params and query_params['user']
        article = 'article' in query_params and query_params['article']
        filter = {
            ['user__pk', 'article__pk'][i]: val for i, val in enumerate([user, article]) if val
        }
        if user or article:
            return ArticleLike.objects.filter(**filter)
        else:
            return ArticleLike.objects.all()

