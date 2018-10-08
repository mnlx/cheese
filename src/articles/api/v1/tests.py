from datetime import timedelta

import pytest
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.urls import reverse
from django.utils import timezone

from articles.models import Article, Author, Category, ArticleLike


User = get_user_model()


def create_author(alias=''):
    user = User.objects.create_user(
        email='test{}@test.com'.format(alias),
        password='secret',
        first_name='Test {}'.format(alias),
        last_name='Tester {}'.format(alias)
    )
    return Author.objects.create(user=user, avatar=ContentFile('picture', name='avatar.jpeg'))


def create_category(alias=''):
    return Category.objects.create(name='category{}'.format(alias))


def create_article(author, category, publish_date, alias=''):
    return Article.objects.create(
        title='Title {}'.format(alias),
        content='Content {}'.format(alias),
        hero=ContentFile('picture', name='hero.jpeg'),
        author=author,
        category=category,
        publish_date=publish_date,
    )


def create_article_like(article, alias=''):
    user = User.objects.create_user(
        email='test{}@test.com'.format(alias),
        password='secret',
        first_name='Test {}'.format(alias),
        last_name='Tester {}'.format(alias)
    )
    return ArticleLike.objects.create(
        user=user,
        article=article
    )


@pytest.mark.django_db(transaction=False)
def test_articles_schema(client):
    author = create_author()
    category = create_category()

    today = timezone.now().date() - timedelta(days=1)
    article = create_article(author, category, today)

    create_article_like(article, 'John')

    url = reverse('articles-list')
    response = client.get(url)

    article_likes_array = [article]
    article = response.json()['results'][0]
    assert list(article.keys()) == [
        'author',
        'category',
        'title',
        'content',
        'hero',
        'slug',
        'publish_date',
        'likes_count',
        'user_like'
    ]

    assert list(article['author'].keys()) == ['slug', 'name', 'avatar']
    assert list(article['category'].keys()) == ['slug', 'name']
    assert int(article['likes_count']) == 1

    # Testing with query ?filter=homepage
    for i in range(2):
        article_likes_array.append(create_article(author, category, today))

    for i in range(len(article_likes_array)):
        for u in range(i):
            create_article_like(article_likes_array[i], f'John_{i}{u}')

    response = client.get(url + '?filter=homepage')
    result = response.json()['results']
    assert int(result[0]['likes_count']) == 2
    assert int(result[1]['likes_count']) == 1
    assert int(result[2]['likes_count']) == 1
