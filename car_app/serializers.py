from rest_framework import serializers

from .models import CarInfo,CustomerInfo,Order,Investment

class CarInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarInfo
        fields = (
            "car_no",
            "maintenance"
        )

class CustomerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInfo
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = '__all__'