from django.test import TestCase
from api.models import Category, Feed, Article, Disease, Site
from datetime import date


"""
These tests are for api.models Models.
"""


class CategoryTestCase(TestCase):

    def setUp(self) -> None:
        self.category = Category.objects.create(name='Category')

    def test_category_name(self):
        self.assertTrue(isinstance(self.category, Category))
        self.assertEqual(self.category.name, 'Category')

    def test_str(self):
        self.assertEqual(str(self.category), 'Category')


class FeedTestCase(TestCase):

    def setUp(self) -> None:
        self.site = Site.objects.create(name='Site', url='www.site.com')
        self.feed = Feed.objects.create(url='www.site/feed.com', missing_fields='I,S', update_time=6,
                                        source_site=self.site)

    def test_feed_url(self):
        self.assertEqual(self.feed.url, 'www.site/feed.com')

    def test_feed_missing_fields(self):
        self.assertEqual(self.feed.missing_fields, 'I,S')

    def test_feed_update_time(self):
        self.assertEqual(self.feed.update_time, 6)

    def test_default_params(self):
        feed = Feed.objects.create(url='www.site/feed.com', missing_fields='I,S', source_site=self.site)

        self.assertEqual(feed.update_time, 24)


class SiteTestCase(TestCase):

    def setUp(self) -> None:
        self.site = Site.objects.create(name='Site', url='www.site.com')

    def test_site_name(self):
        self.assertEqual(self.site.name, 'Site')

    def test_site_url(self):
        self.assertEqual(self.site.url, 'www.site.com')

    def test_str(self):
        self.assertEqual(str(self.site), 'Site')


class DiseaseTestCase(TestCase):

    def setUp(self) -> None:
        self.category = Category.objects.create(name='Category')
        self.disease = Disease.objects.create(name='Disease', category=self.category)

    def test_disease_name(self):
        self.assertEqual(self.disease.name, 'Disease')

    def test_str(self):
        self.assertEqual(str(self.disease), 'Disease')


class ArticleTestCase(TestCase):

    def setUp(self) -> None:
        self.site = Site.objects.create(name='Site', url='www.site.com')
        self.article = Article.objects.create(title='title',
                                              url='www.site/articles/1.com',
                                              summary='this is the summary',
                                              published_date='2000-10-25',
                                              time_to_read=10,
                                              views=1,
                                              likes=1,
                                              clicks=1,
                                              shares=1,
                                              source_site=self.site)

    def test_article_title(self):
        self.assertEqual(self.article.title, 'title')

    def test_article_url(self):
        self.assertEqual(self.article.url, 'www.site/articles/1.com')

    def test_article_summary(self):
        self.assertEqual(self.article.summary, 'this is the summary')

    def test_article_time_to_read(self):
        self.assertEqual(self.article.time_to_read, 10)

    def test_article_views(self):
        self.assertEqual(self.article.views, 1)

    def test_article_likes(self):
        self.assertEqual(self.article.likes, 1)

    def test_article_clicks(self):
        self.assertEqual(self.article.clicks, 1)

    def test_article_shares(self):
        self.assertEqual(self.article.shares, 1)

    def test_default_params(self):
        article = Article.objects.create(title='title',
                                         url='www.site/articles/1.com',
                                         summary='this is the summary',
                                         source_site=self.site)

        self.assertEqual(article.time_to_read, 5)
        self.assertEqual(article.published_date, date.today())
        self.assertEqual(article.views, 0)
        self.assertEqual(article.likes, 0)
        self.assertEqual(article.clicks, 0)
        self.assertEqual(article.shares, 0)

    def test_str(self):
        self.assertEqual(str(self.article), 'title')
