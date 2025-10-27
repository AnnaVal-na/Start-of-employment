from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import TradingNetwork, Product
from .serializers import TradingNetworkSerializer, ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class TradingNetworkViewSet(viewsets.ModelViewSet):
    queryset = TradingNetwork.objects.all()
    serializer_class = TradingNetworkSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['country']
    ordering_fields = '__all__'
    