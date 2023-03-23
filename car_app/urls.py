from django.urls import path
from .import views

urlpatterns = [ 
    path('index/',views.index),
    path('',views.CarData.as_view()),
    # path('customer/',views.CustomerData.as_view()),
    # path('order/',views.OrderData.as_view()),
    path('investment/',views.InvestmentData),
    path('investment/<int:id>/',views.InvestmentData),
    path('order/',views.OrderApi),
    path('order/<int:id>/',views.OrderApi),
    path('order/<int:id>/paid/',views.OrderApi),
    path('customer/',views.CustomerApi),
    path('customer/<int:id>/',views.CustomerApi),
]