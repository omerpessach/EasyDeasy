from .models import Category, Feed, Site, Disease, Article, Model
from rest_framework.serializers import ModelSerializer, CharField
from easydeasy_rest import settings
import os
import random
from typing import Type


def handle_pk_or_str_post(validated_data: dict, value_key: str, model: Type[Model], serializer_key='name') -> dict:
    """
    Checks if the validated data wanted value is pk/different key and modifies the validated data to what's needed!
    """
    value = validated_data[value_key]
    kwargs = {'pk': int(value)} if value.isnumeric() else {serializer_key: value}
    validated_data[value_key] = model.objects.get(**kwargs)

    return validated_data


class DiseaseSerializer(ModelSerializer):
    category = CharField()

    class Meta:
        model = Disease
        fields = '__all__'

    def create(self, validated_data):
        validated_data = handle_pk_or_str_post(validated_data, 'category', Category)
        return super().create(validated_data)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FeedSerializer(ModelSerializer):
    source_site = CharField()

    class Meta:
        model = Feed
        fields = '__all__'

    def create(self, validated_data):
        validated_data = handle_pk_or_str_post(validated_data, 'source_site', Site)
        return super().create(validated_data)


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
