from datetime import timedelta

import pytest
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.urls import reverse
from django.utils import timezone

from articles.models import Article, Author, Category


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


@pytest.mark.django_db(transaction=False)
def test_articles_schema(client):
    author = create_author()
    category = create_category()

    today = timezone.now().date() - timedelta(days=1)
    article = create_article(author, category, today)

    url = reverse('articles-list')
    response = client.get(url)

    article = response.json()[0]
    assert list(article.keys()) == [
        'author',
        'category',
        'title',
        'content',
        'hero',
        'slug',
        'publish_date'
    ]
    assert list(article['author'].keys()) == ['slug', 'name', 'avatar']
    assert list(article['category'].keys()) == ['slug', 'name']
