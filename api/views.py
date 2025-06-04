from urllib import response
from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from storeapp.models import Category, Product, Review
from . import serializers, filters

# Create your views here.

class APIProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['category_id', 'category', 'old_price', 'name',]
    filterset_class = filters.ProductFilter
    search_fields = ["name", "description"]
    ordering_fields = ["old_price"]
    pagination_class = PageNumberPagination

# class APIProductView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    

class APICategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.CategoryFilter

# class APICategoryView(ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

class APIReviewViewSet(ModelViewSet):
    # queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    
    def get_queryset(self):
        Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        context = { "product_id": self.kwargs["product_pk"]}
        return context