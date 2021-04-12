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
        self.serializer = CategorySerializer(instance=self.category)

    def test_contains_expected_fields(self):
        self.assertCountEqual(set(self.category_data.keys()), {'name'})

    def test_valid(self):
        serializer = CategorySerializer(data=self.category_data)

        # Makes sure we can create the site with this data
        self.assertTrue(serializer.is_valid())

    def test_display_serializer(self):
        display_serializer = CategorySerializer(Category.objects.get(name='category_name'))

        category_data = display_serializer.data

        self.assertEquals(category_data['name'], self.category_data['name'])




