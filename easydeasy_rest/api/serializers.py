from .models import Category, Feed, Site, Disease, Article
from rest_framework.serializers import ModelSerializer, CharField
from easydeasy_rest import settings
import os
import random


class DiseaseSerializer(ModelSerializer):
    category = CharField()

    class Meta:
        model = Disease
        fields = '__all__'

    def create(self, validated_data):
        category_value = validated_data['category']

        if category_value.isnumeric():
            validated_data['category'] = Category.objects.get(pk=int(category_value))

        else:
            validated_data['category'] = Category.objects.get(name=category_value)

        return super().create(validated_data)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
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

    def create(self, validated_data):

        # Updates the to generic image if possible
        if validated_data['img'] is None:
            # Gets First Disease in list
            disease: Disease = validated_data['diseases'][0]

            image_folder = f'/images/{disease.category.name}/'
            folder_path = f'{settings.MEDIA_ROOT}{image_folder}'

            # Selects random image
            random_image = random.choice(os.listdir(folder_path))

            validated_data['img'] = f'{image_folder}{random_image}'

        return super(ArticleSerializer, self).create(validated_data)

    class Meta:
        model = Article
        fields = '__all__'
