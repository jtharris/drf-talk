from rest_framework import viewsets, generics, response, status
from beer.models import Beer
from beer.serializers import BeerSerializer, OrderSerializer


class BeerViewSet(viewsets.ModelViewSet):

    queryset = Beer.objects.all()
    serializer_class = BeerSerializer


class OrderView(generics.CreateAPIView):

    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        print('Creating a new order')
        print(serializer.validated_data)

        # TODO:  Add the specific beer and quantity.
        beer_message = 'Enjoy your beer!'

        send_mail(
            subject='Beer Delivery',
            from_email='api@beerdelivery.com',
            recipient_list=[serializer.validated_data['email']],
            message=beer_message
        )

        # TODO:  DEPLOY THE BEER DRONES FOR DELIVERY

