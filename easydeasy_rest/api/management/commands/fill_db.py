from django.core.management.base import BaseCommand
from api.factories import ArticleFactory, DiseaseFactory, CategoryFactory, SiteFactory, FeedFactory, ResearchFactory
from api.models import Disease
import random
from django.db.utils import IntegrityError

# todo - add Feed
# todo - use Disease.objects architecture

# region consts

ARTICLE_AMOUNT = 50
RESEARCH_AMOUNT = 20
DISEASE_AMOUNT = 15
SITE_AMOUNT = 10
FEED_AMOUNT = 20
CATEGORY_AMOUNT = 7

# endregion


class Command(BaseCommand):
    help = 'Fills the database.'

    def handle(self, *args, **options):
        self.call_factory(CategoryFactory, CATEGORY_AMOUNT)

        self.call_factory(DiseaseFactory, DISEASE_AMOUNT)

        self.call_factory(SiteFactory, SITE_AMOUNT)

        self.call_factory(FeedFactory, FEED_AMOUNT)

        self.call_factory(ArticleFactory, ARTICLE_AMOUNT, has_diseases=True)

        self.call_factory(ResearchFactory, RESEARCH_AMOUNT, has_diseases=True)

    @staticmethod
    def call_factory(factory, amount, has_diseases=False):
        """
        Calls the factory amount times and creates new instances for the database.
        :param has_diseases: If the factory has diseases needed to be attached to it
        :param factory: The factory to call
        :param amount: Amount of instances to create
        """
        for _ in range(amount):
            try:
                if has_diseases:
                    factory.create(diseases=(random.choices(Disease.objects.all(), k=random.randrange(1, 4))))
                else:
                    factory.create()
            except IntegrityError as e:
                print(e)
