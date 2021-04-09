from datetime import date

from django.db.models import Model, CASCADE, CharField, DateField, IntegerField, ManyToManyField, ForeignKey, ImageField
from api.utils import parse_image_name_from_path


"""

models.py contains all the models relevant for the api which includes:

- Site
- DefaultCategoryImage
- Category
- Disease
- Article
- Feed

Simple flow -> 
    Aggregator GETs all the sites, from each site he GETs it's feeds to fetch articles, it then POSTs article with it's
    relevant disease and category. 
    
    For each category there's defaults images in case the article entry has no image.

"""


# todo - Add Research model
# todo - research about default category image, is it a good or even an OK method?


class Site(Model):
    """
    Supported sites which we aggregate information from
    """
    name = CharField(max_length=64)
    url = CharField(max_length=256)

    def __str__(self):
        return self.name


class Category(Model):
    """
    Contains diseases and defaults images
    """
    name = CharField(max_length=64)

    def __str__(self):
        return self.name


class Disease(Model):
    """
    Each article has related disease, used for filtering articles by diseases.
    """
    name = CharField(max_length=64, unique=True)

    category = ForeignKey(Category, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Article(Model):
    """
    Used for displaying all the information on the front, being POSTed by aggregator
    """
    title = CharField(max_length=128)
    url = CharField(max_length=512)
    summary = CharField(max_length=1024)
    img = ImageField(upload_to='images/', default=None, blank=True, null=True)
    published_date = DateField(default=date.today)
    time_to_read = IntegerField(default=5)
    views = IntegerField(default=0)
    likes = IntegerField(default=0)
    clicks = IntegerField(default=0)
    shares = IntegerField(default=0)

    source_site = ForeignKey(Site, on_delete=CASCADE, related_name='articles')
    diseases = ManyToManyField(Disease)

    def __str__(self):
        return self.title

    class Meta:
        """
        Used to order the entries by descending published_date
        """
        ordering = ['-published_date']


class Feed(Model):
    """
    Site contains feeds, each feed contains the exact url of the rss feed to parse and it's values relevant for
    the aggregator.
    """
    url = CharField(max_length=512)
    missing_fields = CharField(max_length=128)
    update_time = IntegerField(default=24)

    source_site = ForeignKey(Site, on_delete=CASCADE)