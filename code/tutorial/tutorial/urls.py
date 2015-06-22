from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from beer.views import BeerViewSet, OrderView

router = DefaultRouter()
router.register('beers', BeerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^orders/', OrderView.as_view())
]

