from rest_framework import serializers
from .models import TradingNetwork, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class TradingNetworkSerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source='supplier.name', read_only=True)
    products_detail = ProductSerializer(source='products', many=True, read_only=True)

    class Meta:
        model = TradingNetwork
        fields = '__all__'
        read_only_fields = ('debt_to_supplier',)
