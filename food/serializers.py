from django.core.validators import MinLengthValidator
from rest_framework import serializers
from food.validators import validate_image

from food.models import Product


class ProductInputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, validators=[MinLengthValidator(2)])
    image = serializers.ImageField(validators=[validate_image], required=False)
    calories_per_100_g = serializers.DecimalField(max_digits=5, decimal_places=2)
    proteins_per_100_g = serializers.DecimalField(max_digits=5, decimal_places=2)
    carbohydrates_per_100_g = serializers.DecimalField(max_digits=5, decimal_places=2)
    fats_per_100_g = serializers.DecimalField(max_digits=5, decimal_places=2)
    fiber_per_100_g = serializers.DecimalField(max_digits=5, decimal_places=2)
    is_vegetarian = serializers.BooleanField(default=False)
    is_vegan = serializers.BooleanField(default=False)
    is_keto_friendly = serializers.BooleanField(default=False)
    is_gluten_free = serializers.BooleanField(default=False)
    is_lactose_free = serializers.BooleanField(default=False)
    is_nut_free = serializers.BooleanField(default=False)
    is_soy_free = serializers.BooleanField(default=False)
    is_shellfish_free = serializers.BooleanField(default=False)


class ProductOutputSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = ["added_by", "is_verified"]

    def get_image(self, product: Product) -> str:
        return product.image.url if product.image else None
