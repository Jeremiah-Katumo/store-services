from django.urls import path
from . import views

urlpatterns = [
    path("products", views.APIProductsView.as_view(), name="api_products"),
    path("products/<str:pk>", views.APIProductView.as_view(), name="api_product"),
    path("categories", views.APICategoriesView.as_view(), name="api_categories"),
    path("categories/<str:pk>", views.APICategoryView.as_view(), name="api_category"),
]