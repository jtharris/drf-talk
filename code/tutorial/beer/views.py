import textwrap
from django.core.mail import send_mail
from rest_framework import viewsets, generics, response, status
from beer.models import Beer
from beer.serializers import BeerSerializer, OrderSerializer


class BeerViewSet(viewsets.ModelViewSet):

    queryset = Beer.objects.all()
    serializer_class = BeerSerializer


class OrderView(generics.CreateAPIView):

    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        beer_message = textwrap.dedent("""\
            Enjoy your beer!

            Beer Type:  {beer}
            Quantity:   {quantity}""").format(**serializer.validated_data)

        send_mail(
            subject='Beer Delivery',
            from_email='api@beerdelivery.com',
            recipient_list=[serializer.validated_data['email']],
            message=beer_message
        )

        # TODO:  DEPLOY THE BEER DRONES FOR DELIVERY

