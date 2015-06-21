from rest_framework.routers import DefaultRouter
from beer.views import BeerViewSet

router = DefaultRouter()
router.register('beers', BeerViewSet)
urlpatterns = router.urls

