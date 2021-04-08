from django.core.management.base import BaseCommand
from api.factories import ArticleFactory, DiseaseFactory, CategoryFactory, SiteFactory
from api.models import Disease
import random
from django.db.utils import IntegrityError

# todo - add Feed
# todo - use Disease.objects architecture

# region consts

ARTICLE_AMOUNT = 50
DISEASE_AMOUNT = 15
SITE_AMOUNT = 10
CATEGORY_AMOUNT = 7

# endregion


class Command(BaseCommand):
    help = 'Fills the database.'

    def handle(self, *args, **options):
        self.call_factory(CategoryFactory, CATEGORY_AMOUNT)

        self.call_factory(DiseaseFactory, DISEASE_AMOUNT)

        self.call_factory(SiteFactory, SITE_AMOUNT)

        self.call_factory(ArticleFactory, ARTICLE_AMOUNT, is_article=True)

    @staticmethod
    def call_factory(factory, amount, is_article=False):
        """
        Calls the factory amount times and creates new instances for the database.
        :param is_article: If it's article factory
        :param factory: The factory to call
        :param amount: Amount of instances to create
        """
        for _ in range(amount):
            try:
                if is_article:
                    factory.create(diseases=(random.choices(Disease.objects.all(), k=random.randrange(3))))
                else:
                    factory.create()
            except IntegrityError as e:
                print(e)
