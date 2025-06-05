from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views


router = DefaultRouter()
router.register(r'products', views.APIProductView, basename='products')
router.register(r'categories', views.APICategoryView, basename='categories')
router.register(r'carts', viewset=views.APICartViewSet, basename='carts')

product_router = routers.NestedDefaultRouter(router, r'products', lookup='product')
product_router.register(r'reviews', views.APIReviewViewSet, basename="product_reviews")

urlpatterns = router.urls


urlpatterns = [
    path("", include(router.urls)),
    path("", include(product_router.urls))
    # path("products", views.APIProductsView.as_view(), name="api_products"),
    # path("products/<str:pk>", views.APIProductView.as_view(), name="api_product"),
    # path("categories", views.APICategoriesView.as_view(), name="api_categories"),
    # path("categories/<str:pk>", views.APICategoryView.as_view(), name="api_category"),
]