from django.core.validators import FileExtensionValidator
from django.db import models

from food.models import Product, Dish


class ProductImage(models.Model):
    image = models.ImageField(
        upload_to="product_images/",
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "png"])],
    )
    product = models.OneToOneField(Product, on_delete=models.CASCADE)


class DishImage(models.Model):
    image = models.ImageField(
        upload_to="dish_images/",
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "png"])],
    )
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)
