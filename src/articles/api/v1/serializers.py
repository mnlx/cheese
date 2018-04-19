from rest_framework import serializers

from articles.models import Article, Author, Category


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


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer()

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
        )
