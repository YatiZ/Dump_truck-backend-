from django.shortcuts import render
from .models import CarInfo,CustomerInfo,Investment,Order
from .serializers import CarInfoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

def index(request):
    orders = Order.objects.all()
    carinfo = CarInfo.objects.all()
    context = {'carinfo':carinfo,'orders':orders}
    return render(request,'index.html',context,)

class CarData(APIView):
    def get(self,request,format = None):
        carinfo = CarInfo.objects.all()
        serializer = CarInfoSerializer(carinfo,many=True)
        return Response(serializer.data)