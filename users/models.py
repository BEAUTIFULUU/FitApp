import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from users.choices.activity_choices import ACTIVITY_CHOICES


class CustomUser(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True)
    birth_date = models.DateField()
    weight = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(20), MaxValueValidator(800)],
    )
    height = models.DecimalField(
        max_digits=3,
        decimal_places=0,
        validators=[MinValueValidator(100), MaxValueValidator(300)],
    )
    activity = models.CharField(choices=ACTIVITY_CHOICES)


class Summary(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True)
    date = models.DateField()
    calories = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    proteins = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    carbohydrates = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    fats = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    fiber = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="summaries"
    )

    def __str__(self):
        return f"Summary on {self.date}"
