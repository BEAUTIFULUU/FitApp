from typing import Type

from django.db.models import QuerySet
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from food.models import Product
from food.services import list_products, create_product
from food.serializers import ProductInputSerializer, ProductOutputSerializer
from images.services import create_product_image


class ProductView(generics.ListCreateAPIView):
    filterset_fields = {
        "calories_per_100_g": ["exact", "gte", "lte"],
        "proteins_per_100_g": ["exact", "gte", "lte"],
        "carbohydrates_per_100_g": ["exact", "gte", "lte"],
        "fats_per_100_g": ["exact", "gte", "lte"],
        "fiber_per_100_g": ["exact", "gte", "lte"],
        "is_vegetarian": ["exact"],
        "is_vegan": ["exact"],
        "is_keto_friendly": ["exact"],
        "is_gluten_free": ["exact"],
        "is_lactose_free": ["exact"],
        "is_nut_free": ["exact"],
        "is_soy_free": ["exact"],
        "is_shellfish_free": ["exact"],
        "is_high_protein": ["exact"],
        "is_low_sugar": ["exact"],
    }

    def get_serializer_class(
        self,
    ) -> Type[ProductOutputSerializer | ProductInputSerializer]:
        return (
            ProductOutputSerializer
            if self.request.method == "GET"
            else ProductInputSerializer
        )

    def get_queryset(self) -> QuerySet[Product]:
        return list_products()

    def create(self, request: Request, *args, **kwargs) -> Response:
        product_image = request.FILES.get("image")
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        created_product = create_product(
            data=serializer.validated_data, user=self.request.user
        )
        if product_image is not None:
            create_product_image(image=product_image, product=created_product)
        output_serializer = ProductOutputSerializer(created_product)
        return Response(data=output_serializer.data, status=status.HTTP_201_CREATED)
