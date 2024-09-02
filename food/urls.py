from django.urls import path
from food.views import ProductView

urlpatterns = [path("products/", ProductView.as_view(), name="list_products")]
