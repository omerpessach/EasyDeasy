from .models import Category, DefaultCategoryImage, Feed, Site, Disease, Article
from rest_framework.serializers import ModelSerializer


class DiseaseSerializer(ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DefaultCategoryImageSerializer(ModelSerializer):
    class Meta:
        model = DefaultCategoryImage
        fields = '__all__'


class FeedSerializer(ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'


class SiteSerializer(ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

