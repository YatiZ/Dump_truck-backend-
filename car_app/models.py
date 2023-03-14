from django.db import models
import uuid
from datetime import datetime
# Create your models here.

# class CarInfo(models.TextChoices):
#     FIRST_CAR = "1P",'1P'
#     SECOND_CAR = "7Q",'7Q'
#     THIRD_CAR = "5R",'5R'

class CarInfo(models.Model):
    car_no = models.TextField(max_length=50)
    maintenance =  models.TextField(blank=True)
    # def __str__(self):
    #     return self.car_no

class CustomerInfo(models.Model):
    customer_name = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(blank=True,null=True)
    phone_no = models.TextField(max_length=50, blank=True)
    address = models.TextField(max_length=100, blank= True)
    def __str__(self):
        return f"{self.customer_name}{self.created_at}"

class Order(models.Model):
    car_id = models.ForeignKey(CarInfo,blank=True,on_delete=models.CASCADE)
    customer_id = models.ForeignKey(CustomerInfo,blank=True,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(blank=True,null=True)
    count = models.IntegerField(blank=True)
    service_fees_per_count = models.TextField(max_length=100,blank=True)
    debt_amount = models.TextField(max_length=100,blank=True)
    description = models.TextField(max_length=200, blank=True)
    paid_amount = models.TextField(max_length=100,blank=True)
    

class Investment(models.Model):
    car_id =  models.ForeignKey(CarInfo,blank=True,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(blank=True,null=True)
    petrol = models.TextField(blank=True)
    driver_fees = models.TextField()
    extra_cost = models.TextField(blank=True)
    cost_for_home = models.TextField()


    





