from rest_framework.test import APITestCase
from api.serializers import CategorySerializer, FeedSerializer, ArticleSerializer, DiseaseSerializer, SiteSerializer
from api.models import Category, Feed, Article, Disease, Site

"""
These tests are for api.serializers Serializers.
"""


# Create your tests here.


class CategorySerializersTests(APITestCase):

    def setUp(self):
        self.category_data = {'name': 'category_name'}

        self.category = Category.objects.create(**self.category_data)

    def test_contains_expected_fields(self):
        self.assertCountEqual(set(self.category_data.keys()), {'name'})

    def test_valid(self):
        serializer = CategorySerializer(data=self.category_data)

        self.assertTrue(serializer.is_valid())

    def test_display_serializer(self):
        display_serializer = CategorySerializer(self.category)

        category_data = display_serializer.data

        self.assertEquals(category_data['name'], self.category_data['name'])


class FeedSerializersTests(APITestCase):

    def setUp(self):
        self.source_site = Site.objects.create(name='site', url='www.mysite.com')

        self.feed_data = {'url': 'www.site/feeds/my-feed.com',
                          'missing_fields': 'I',
                          'update_time': 10,
                          'source_site': self.source_site.pk}

        self.feed = Feed.objects.create(**self.feed_data | {'source_site': self.source_site})

    def test_contains_expected_fields(self):
        self.assertCountEqual(set(self.feed_data.keys()), {'url', 'missing_fields', 'update_time', 'source_site'})

    def test_valid(self):
        serializer = FeedSerializer(data=self.feed_data)

        self.assertTrue(serializer.is_valid())

    def test_display_serializer(self):
        display_serializer = FeedSerializer(self.feed)

        feed_data = display_serializer.data

        self.assertEquals(feed_data['url'], self.feed_data['url'])
        self.assertEquals(feed_data['missing_fields'], self.feed_data['missing_fields'])
        self.assertEquals(feed_data['update_time'], self.feed_data['update_time'])
        self.assertEquals(feed_data['source_site'], self.feed_data['source_site'])


class ArticleSerializersTests(APITestCase):

    def setUp(self):
        self.source_site = Site.objects.create(name='site', url='www.mysite.com')

        self.category = Category.objects.create(name='serializer_category')

        self.disease_1 = Disease.objects.create(name='disease_1', category=self.category)
        self.disease_2 = Disease.objects.create(name='disease_2', category=self.category)

        self.article_data = {'title': 'best article',
                             'url': 'www.website/articles-best.com',
                             'summary': 'test serializer summary',
                             'published_date': '2020-02-18',
                             'time_to_read': 8,
                             'likes': 25,
                             'clicks': 25,
                             'shares': 5,
                             'views': 87,
                             'source_site': self.source_site.pk}

        self.article = Article.objects.create(**self.article_data | {'source_site': self.source_site})
        self.article.diseases.set([self.disease_1, self.disease_2])

    def test_contains_expected_fields(self):
        self.assertCountEqual(set(self.article_data.keys()), {'title', 'url', 'summary', 'published_date',
                                                              'time_to_read', 'likes', 'clicks', 'shares',
                                                              'views', 'source_site'})

    def test_valid(self):
        serializer = ArticleSerializer(data=self.article_data | {'diseases': [self.disease_1.pk, self.disease_2.pk]})

        self.assertTrue(serializer.is_valid())

    def test_display_serializer(self):
        display_serializer = ArticleSerializer(self.article)

        article_data = display_serializer.data

        self.assertEquals(article_data['title'], self.article_data['title'])
        self.assertEquals(article_data['url'], self.article_data['url'])
        self.assertEquals(article_data['summary'], self.article_data['summary'])
        self.assertEquals(article_data['published_date'], self.article_data['published_date'])
        self.assertEquals(article_data['time_to_read'], self.article_data['time_to_read'])
        self.assertEquals(article_data['likes'], self.article_data['likes'])
        self.assertEquals(article_data['clicks'], self.article_data['clicks'])
        self.assertEquals(article_data['shares'], self.article_data['shares'])
        self.assertEquals(article_data['views'], self.article_data['views'])
        self.assertEquals(article_data['source_site'], self.article_data['source_site'])


class DiseaseSerializersTests(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(name='disease_category')

        self.disease_data = {'name': 'test_disease',
                             'category': self.category.pk}

        self.disease = Disease.objects.create(**self.disease_data | {'category': self.category})

    def test_contains_expected_fields(self):
        self.assertCountEqual(set(self.disease_data.keys()), {'name', 'category'})

    def test_valid(self):
        serializer = DiseaseSerializer(data=self.disease_data | {'name': 'different_disease'})
        non_unique_serializer = DiseaseSerializer(data=self.disease_data)

        self.assertTrue(serializer.is_valid())
        self.assertFalse(non_unique_serializer.is_valid())

    def test_display_serializer(self):
        display_serializer = DiseaseSerializer(self.disease)

        disease_data = display_serializer.data

        self.assertEquals(disease_data['name'], self.disease_data['name'])
        self.assertEquals(disease_data['category'], self.disease_data['category'])


class SiteSerializersTests(APITestCase):

    def setUp(self):
        self.site_data = {'name': 'site',
                          'url': 'www.mysite.com'}

        self.site = Site.objects.create(name='site', url='www.mysite.com')

    def test_contains_expected_fields(self):
        self.assertCountEqual(set(self.site_data.keys()), {'name', 'url'})

    def test_valid(self):
        serializer = SiteSerializer(data=self.site_data)

        self.assertTrue(serializer.is_valid())

    def test_display_serializer(self):
        display_serializer = SiteSerializer(self.site)

        site_data = display_serializer.data

        self.assertEquals(site_data['name'], self.site_data['name'])
        self.assertEquals(site_data['url'], self.site_data['url'])
