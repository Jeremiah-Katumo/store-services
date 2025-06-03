from urllib import response
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, APIView
from .serializers import ProductSerializer, CategorySerializer
from storeapp.models import Category, Product
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

from . import serializers, filters

# Create your views here.

class APIProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['category_id', 'category', 'old_price', 'name',]
    filteset_class = filters.ProductFilter

# class APIProductView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    

class APICategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# class APICategoryView(ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
