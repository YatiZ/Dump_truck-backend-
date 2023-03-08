from django.shortcuts import render
from .models import CarInfo,CustomerInfo,Investment,Order
from .serializers import CarInfoSerializer,CustomerInfoSerializer,OrderSerializer,InvestmentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


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

class CustomerData(APIView):
    def get(self,request):
        customer_data = CustomerInfo.objects.all()
        serializer = CustomerInfoSerializer(customer_data,many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CustomerInfoSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class OrderData(APIView):
    def get(self,request):
        order_data = Order.objects.all()
        serializer = OrderSerializer(order_data, many= True)
        return Response(serializer.data)

    def post(self,request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def InvestmentData(request):
    method = request.method
    if method == 'GET':
        get_data = Investment.objects.all()
        serializer = InvestmentSerializer(get_data, many=True)
        return Response(serializer.data)
    if method == 'POST':
        serializer = InvestmentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
