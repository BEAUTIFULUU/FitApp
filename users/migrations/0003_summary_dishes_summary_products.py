# Generated by Django 5.1 on 2024-08-22 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0002_dish_image"),
        ("users", "0002_alter_userprofile_activity_alter_userprofile_goal"),
    ]

    operations = [
        migrations.AddField(
            model_name="summary",
            name="dishes",
            field=models.ManyToManyField(related_name="summaries", to="food.dish"),
        ),
        migrations.AddField(
            model_name="summary",
            name="products",
            field=models.ManyToManyField(related_name="summaries", to="food.product"),
        ),
    ]
