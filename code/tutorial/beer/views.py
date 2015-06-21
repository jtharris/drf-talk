from rest_framework import viewsets
from beer.models import Beer
from beer.serializers import BeerSerializer


class BeerViewSet(viewsets.ModelViewSet):

    queryset = Beer.objects.all()
    serializer_class = BeerSerializer

