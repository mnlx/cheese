from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.validators import UniqueTogetherValidator
from articles.models import Article, Author, Category, ArticleLike


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
        model = ArticleLike
        fields = (
            'user',
            'article'
        )
        validators = [
            UniqueTogetherValidator(
                queryset=ArticleLike.objects.all(),
                fields=('user', 'article'),
                message='User and article pair is not unique.'
            )
        ]


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer()
    likes_count = SerializerMethodField(read_only=True)
    user_like_id = SerializerMethodField(read_only=True)

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
            'likes_count',
            'user_like_id'
        )

    def get_likes_count(self, obj):
        return obj.articlelike_set.count()

    def get_user_like_id(self, obj):
        request = self.context.get('request')
        user_id = request.user.id
        articles_like_result = obj.articlelike_set.filter(user__pk=user_id)
        return len(articles_like_result) and articles_like_result[0].id
