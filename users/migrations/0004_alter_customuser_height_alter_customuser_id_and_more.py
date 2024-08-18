# Generated by Django 5.1 on 2024-08-18 16:55

import django.core.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_customuser_name_customuser_surname_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="height",
            field=models.DecimalField(
                decimal_places=0,
                max_digits=5,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(100),
                    django.core.validators.MaxValueValidator(300),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("3bf75de9-2b89-46e3-b00c-0b1c7de47866"),
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="weight",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=5,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(20),
                    django.core.validators.MaxValueValidator(800),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="summary",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("c073b82f-fe3c-40d5-9c7f-50681fac0210"),
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
