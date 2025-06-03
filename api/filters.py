from django_filters.rest_framework import FilterSet
from storeapp.models import Product, Category

class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'category_id': ['exact'],
            'old_price': ['lt', 'gt', 'exact'],
            'name': ['icontains'],
        }
        
class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields = {
            'title': ['icontains'],
            'slug': ['exact'],
        }