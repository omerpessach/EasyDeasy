from rest_framework.viewsets import ModelViewSet
from .models import Category, DefaultCategoryImage, Feed, Site, Disease, Article
from .serializers import DefaultCategoryImageSerializer, SiteSerializer, DiseaseSerializer, ArticleSerializer, \
    FeedSerializer, CategorySerializer


class SiteViewSet(ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class DiseaseViewSet(ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class FeedViewSet(ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer


class DefaultCategoryImageViewSet(ModelViewSet):
    queryset = DefaultCategoryImage.objects.all()
    serializer_class = DefaultCategoryImageSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
