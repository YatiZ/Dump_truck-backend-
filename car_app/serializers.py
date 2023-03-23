from rest_framework import serializers

from .models import CarInfo,CustomerInfo,Order,Investment

class CarInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarInfo
        fields = (
            "id",
            "car_no",
            "maintenance"
        )

class CustomerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInfo
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    customer_id = CustomerInfoSerializer()
    car_id = CarInfoSerializer(read_only = True)
    class Meta:
        model = Order
        # fields = '__all__'
        fields = (
            "id",
            "car_id",
            "customer_id",
            "created_at",
            "updated_at",
            "deleted_at",
            "count",
            "service_fees_per_count",
            "debt_amount",
            "description",
            "paid_amount",
            "paid",
            "debt"

        )

class SecondOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
    # def create(self, validated_data):
    #     car_id = self.context.get('car_id')
    #     validated_data['car_id'] = CarInfo.objects.get(id=car_id)
    #     return super().create(validated_data)
    

class InvestmentSerializer(serializers.ModelSerializer):
    car_id = CarInfoSerializer()
    class Meta:
        model = Investment
        fields = '__all__'

class PostInvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = '__all__'