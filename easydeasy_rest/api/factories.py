import factory
from api.models import Site, Category, Disease, Article, Feed
from datetime import datetime
import random

# region consts

TIME_TO_READ_AMOUNT = range(1, 15)
SOCIAL_AMOUNT = range(100)


# endregion


class SiteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Site

    name = factory.LazyAttribute(lambda _: f'website_{random.randrange(1000)}')
    url = factory.LazyAttribute(lambda site: f'www.{site.name}.com')


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('random_element', elements=['Cancer', 'Eye', 'Skin', 'Stomach', 'Heart', 'Brain', 'Hair'])


class DiseaseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Disease

    name = factory.Faker('random_element',
                         elements=['Colitis', 'Crohn', 'Covid19', 'Skin cancer', 'Dermatitis', 'Eye cancer',
                                   'Liver cancer', 'Kidney cancer', 'IBS', 'Leukemia', 'Autism', 'Epilepsy',
                                   'Gluten allergy', 'Lactose Intolerance'])

    category = factory.SubFactory(CategoryFactory)


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    source_site = factory.SubFactory(SiteFactory)

    title = factory.LazyAttribute(lambda _: f'article_{random.randrange(1000)}')
    url = factory.LazyAttribute(lambda article: f'www.{article.source_site.name}/articles/{article.title}.com')
    summary = factory.Faker('text')
    published_date = factory.LazyFunction(datetime.now)
    img = None
    time_to_read = factory.Faker('random_element', elements=TIME_TO_READ_AMOUNT)
    views = factory.Faker('random_element', elements=SOCIAL_AMOUNT)
    likes = factory.Faker('random_element', elements=SOCIAL_AMOUNT)
    clicks = factory.Faker('random_element', elements=SOCIAL_AMOUNT)
    shares = factory.Faker('random_element', elements=SOCIAL_AMOUNT)

    @factory.post_generation
    def diseases(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of diseases were passed in, use them
            for disease in extracted:
                self.diseases.add(disease)


class FeedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Feed

    # todo
