from rest_framework import serializers
from beer.models import Beer


class BeerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Beer
