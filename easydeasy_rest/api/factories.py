import factory
from api.models import Site, Category, Disease, Article, Feed, Research
from datetime import datetime
import random

# region consts

TIME_TO_READ_AMOUNT = range(1, 15)
UPDATE_TIME_AMOUNT = range(1, 168)
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

    category = factory.Iterator(Category.objects.all())


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    source_site = factory.Iterator(Site.objects.all())

    title = factory.LazyAttribute(lambda _: f'article_{random.randrange(100)}')
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


class ResearchFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Research

    publisher = factory.Iterator(Site.objects.all())

    title = factory.LazyAttribute(lambda _: f'research_{random.randrange(100)}')
    summary = factory.Faker('text')
    published_date = factory.LazyFunction(datetime.now)
    authors = factory.LazyAttribute(lambda _: ','.join(random.choices(['Anat L', 'Daniel B', 'Moshe G', 'Kelly D',
                                                                       'Stock R', 'Paz B', 'Paz Be', 'Almog E',
                                                                       'Shimrit C', 'Fadid L', 'Alon H', 'Ran D',
                                                                       'Roni K', 'Ido D', 'Omri G'],
                                                                      k=random.randrange(6))))
    url = factory.LazyAttribute(lambda research: f'www.{research.publisher.name}/researchs/{research.title}.com')
    pm_id = factory.LazyAttribute(lambda _: str(random.randint(10000000, 99999999)))

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

    url = factory.LazyAttribute(lambda feed: f'www.{feed.source_site}/feeds/{random.randrange(1000)}.com')
    missing_fields = factory.LazyAttribute(lambda feed: ','.join(random.choices(['I', 'S', 'T'])))
    update_time = factory.Faker('random_element', elements=UPDATE_TIME_AMOUNT)

    source_site = factory.Iterator(Site.objects.all())


