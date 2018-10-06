from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.validators import UniqueTogetherValidator

from articles.models import Article, Author, Category, ArticleLikes



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'slug',
            'name',
            'avatar',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'slug',
            'name',
        )


class ArticleLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleLikes
        fields = (
            'user',
            'article'
        )
        validators = [
            UniqueTogetherValidator(
                queryset=ArticleLikes.objects.all(),
                fields=('user', 'article'),
                message='User and article pair is not unique.'
            )
        ]

class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer()
    likes_count = SerializerMethodField(read_only=True)

    class Meta:
        model = Article
        fields = (
            'author',
            'category',
            'title',
            'content',
            'hero',
            'slug',
            'publish_date',
            'likes_count'
        )


    def get_likes_count(self,obj):
        return obj.articlelikes_set.count()



