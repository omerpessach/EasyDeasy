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

        # Makes sure we can create the site with this data
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

        # Makes sure we can create the site with this data
        self.assertTrue(serializer.is_valid())

    def test_display_serializer(self):
        display_serializer = FeedSerializer(self.feed)

        feed_data = display_serializer.data

        self.assertEquals(feed_data['url'], self.feed_data['url'])
        self.assertEquals(feed_data['missing_fields'], self.feed_data['missing_fields'])
        self.assertEquals(feed_data['update_time'], self.feed_data['update_time'])
        self.assertEquals(feed_data['source_site'], self.feed_data['source_site'])




