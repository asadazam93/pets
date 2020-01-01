from django.conf.urls import url, include
from rest_framework import routers

from animals.views import CatViewSet, DogViewSet

app_name = 'animals'

router = routers.DefaultRouter()

router.register(r'cats', CatViewSet, basename='cats')
router.register(r'dogs', DogViewSet, basename='dogs')

urlpatterns = [
    url(r'^', include(router.urls)),
]