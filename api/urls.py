from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'products', views.APIProductView, basename='api_products')
router.register(r'categories', views.APICategoryView, basename='api_categories')
urlpatterns = router.urls


urlpatterns = [
    path("", include(router.urls))
    # path("products", views.APIProductsView.as_view(), name="api_products"),
    # path("products/<str:pk>", views.APIProductView.as_view(), name="api_product"),
    # path("categories", views.APICategoriesView.as_view(), name="api_categories"),
    # path("categories/<str:pk>", views.APICategoryView.as_view(), name="api_category"),
]