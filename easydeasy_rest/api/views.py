from rest_framework import viewsets
from .models import Category, DefaultCategoryImage, Feed, Site, Disease, Article


class SiteViewSet(ForeignKeyViewSet):
    queryset = Site.objects.all()
    display_serializer = SiteDisplaySerializer
    create_serializer = SiteCreateSerializer


class FeedViewSet(ForeignKeyViewSet):
    queryset = Feed.objects.all()
    display_serializer = FeedDisplaySerializer
    create_serializer = FeedCreateSerializer


class DefaultCategoryImageViewSet(viewsets.ModelViewSet):
    queryset = DefaultCategoryImage.objects.all()
    serializer_class = DefaultCategoryImageSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer