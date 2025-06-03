from urllib import response
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, APIView
from .serializers import ProductSerializer, CategorySerializer
from storeapp.models import Category, Product
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status

from api import serializers

# Create your views here.

class APIProductsView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class APIProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class APICategoriesView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class APICategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
