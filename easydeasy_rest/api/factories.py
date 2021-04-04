import factory
from api.models import Site, Category, Disease, Article, Feed
from datetime import datetime
import random


class SiteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Site

    name = factory.Sequence(lambda i: f'website_{i}')
    url = factory.LazyAttribute(lambda site: f'www.{site.name}.com')


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = random.choice(
        ['Cancer', 'Eye', 'Skin', 'Stomach', 'Heart']
    )


class DiseaseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Disease

    name = random.choice(
        ['Colitis', 'Crohn', 'Covid19', 'Skin cancer', 'Dermatitis', 'Eye cancer', 'Liver cancer', 'Kidney cancer',
         'IBS', 'Leukemia', 'Autism', 'Epilepsy', 'Gluten allergy', 'Lactose Intolerance']
    )

    category = factory.SubFactory(CategoryFactory)


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    source_site = factory.SubFactory(SiteFactory)
    diseases = factory.SubFactory(DiseaseFactory)

    title = factory.Sequence(lambda i: f'article_{i}')
    url = factory.LazyAttribute(lambda article: f'www.{article.source_site.name}/articles/{article.title}.com')
    summary = factory.Faker('text')
    date_joined = factory.LazyFunction(datetime.now)
    img = None
    time_to_read = random.randint(1, 15)
    views = random.randrange(100)
    likes = random.randrange(100)
    clicks = random.randrange(100)
    shares = random.randrange(100)


class FeedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Feed

