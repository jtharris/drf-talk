from rest_framework import serializers
from beer.models import Beer


class BeerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Beer


class OrderSerializer(serializers.Serializer):

    beer = serializers.HyperlinkedRelatedField(view_name='beer-detail', queryset=Beer.objects.all())
    quantity = serializers.IntegerField(min_value=1, max_value=12)
    email = serializers.EmailField()
