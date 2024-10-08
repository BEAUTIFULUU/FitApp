import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

from food.models import Product, Dish
from users.choices import ACTIVITY_CHOICES, GOAL_CHOICES


class UserProfile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=60, null=True)
    surname = models.CharField(max_length=60, null=True)
    birth_date = models.DateField(null=True)
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(20), MaxValueValidator(800)],
        null=True,
    )
    height = models.DecimalField(
        max_digits=5,
        decimal_places=0,
        validators=[MinValueValidator(100), MaxValueValidator(300)],
        null=True,
    )
    activity = models.CharField(choices=ACTIVITY_CHOICES, max_length=50, null=True)
    goal = models.CharField(choices=GOAL_CHOICES, default="Maintain", max_length=50, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Summary(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    date = models.DateField()
    calories = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    proteins = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    carbohydrates = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    fats = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    fiber = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="summaries"
    )
    products = models.ManyToManyField(Product, related_name="summaries")
    dishes = models.ManyToManyField(Dish, related_name="summaries")

