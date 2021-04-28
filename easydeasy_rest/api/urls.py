from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('articles', views.ArticleViewSet)
router.register('diseases', views.DiseaseViewSet)
router.register('sites', views.SiteViewSet)
router.register('feeds', views.FeedViewSet)
router.register('categories', views.CategoryViewSet)
router.register('researches', views.ResearchViewSet)

urlpatterns = [
    path('', include(router.urls))
]
