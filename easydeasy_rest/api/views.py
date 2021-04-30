from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Category, Feed, Site, Disease, Article
from .serializers import SiteSerializer, DiseaseSerializer, ArticleSerializer, \
    FeedSerializer, CategorySerializer


class SiteViewSet(ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class DiseaseViewSet(ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

    @action(detail=False, url_path='(?P<url_disease_id>[0-9]+)/latest_articles')
    def latest_disease_articles(self, request, url_disease_id):
        """ returns the list of newest articles.

            (?P<url_disease_id>[0-9]+) in the decorator forces to only receive ints for url_disease_id.
            """

        # Converts string url to int
        disease_id = int(url_disease_id)

        article_queryset = Article.objects.filter(diseases__id=disease_id)

        # A pagination class used specifically to page the latest articles based on there dates
        class LatestArticlesSetPagination(PageNumberPagination):
            page_size = 10

        pagination = LatestArticlesSetPagination()

        page = pagination.paginate_queryset(article_queryset, request)

        serializer = ArticleSerializer(page, many=True, context={'request': request})
        return pagination.get_paginated_response(serializer.data)


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class FeedViewSet(ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

