from django.contrib.auth.models import User
from django.core.validators import (
    MinLengthValidator,
    FileExtensionValidator,
    MinValueValidator,
)
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    image = models.ImageField(
        upload_to="product_images/",
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "png"])],
        null=True,
    )
    calories_per_100_g = models.DecimalField(max_digits=5, decimal_places=2)
    proteins_per_100_g = models.DecimalField(max_digits=5, decimal_places=2)
    carbohydrates_per_100_g = models.DecimalField(max_digits=5, decimal_places=2)
    fats_per_100_g = models.DecimalField(max_digits=5, decimal_places=2)
    fiber_per_100_g = models.DecimalField(max_digits=5, decimal_places=2)
    is_vegetarian = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_keto_friendly = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    is_lactose_free = models.BooleanField(default=False)
    is_nut_free = models.BooleanField(default=False)
    is_soy_free = models.BooleanField(default=False)
    is_shellfish_free = models.BooleanField(default=False)
    is_high_protein = models.BooleanField(default=False)
    is_low_sugar = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    added_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True)


class Dish(models.Model):
    name = models.CharField(max_length=70, validators=[MinLengthValidator(3)])
    image = models.ImageField(
        upload_to="images/",
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "png"])],
        null=True,
    )
    description = models.TextField()
    preparation_time = models.DurationField()
    is_verified = models.BooleanField(default=False)
    added_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    products = models.ManyToManyField(Product, related_name="dishes")
