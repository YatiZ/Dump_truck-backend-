from django.urls import path
from .import views

urlpatterns = [ 
    path('index/',views.index),
    path('',views.CarData.as_view()),
    path('customer/',views.CustomerData.as_view()),
    path('order/',views.OrderData.as_view()),
    path('investment/',views.InvestmentData)
]