from django.urls import path, include
from rest_framework import routers
from .views import LoginView

router = routers.DefaultRouter()
router.register('login', LoginView)

urlpatterns = [
    path('', include(router.urls))
]
