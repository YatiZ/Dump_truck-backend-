from django.shortcuts import render
from .models import CarInfo,CustomerInfo,Investment,Order
from .serializers import CarInfoSerializer,CustomerInfoSerializer,OrderSerializer,InvestmentSerializer
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
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


@csrf_exempt
def CustomerApi(request, id=0):
    if request.method == 'GET':
        customer_data = CustomerInfo.objects.all()
        customer_serializer = CustomerInfoSerializer(customer_data, many=True)
        return JsonResponse(customer_serializer.data, safe=False)
    elif request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerInfoSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse("Added Successfully",safe= False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method == 'PUT':
        customer_data = JSONParser().parse(request)
        customer = CustomerInfo.objects.get(id = id)
        customer_serializer = CustomerInfoSerializer(customer,data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        customer = CustomerInfo.objects.get(id = id)
        customer.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    

@csrf_exempt
def OrderApi(request, id=0):
    if request.method == 'GET':
        order_data = Order.objects.all()
        order_serializer = OrderSerializer(order_data, many=True)
        return JsonResponse(order_serializer.data, safe= False)
    elif request.method == 'POST':
        order_data = JSONParser().parse(request)
        order_serializer = OrderSerializer(data=order_data)
        if order_serializer.is_valid():
            order_serializer.save()
            return JsonResponse("AddedSuccessfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method == 'PUT':
        order_data = JSONParser().parse(request)
        order = Order.objects.get(id = id)
        order_serializer = OrderSerializer(order, data= order_data)
        if order_serializer.is_valid():
            order_serializer.save()
            return JsonResponse("Update Successfully",safe= False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        order = Order.objects.get(id = id)
        order.delete()
        return JsonResponse("Deleted Successfully",safe = False)
    

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



