from django.contrib.auth.models import User
from django.db.models import QuerySet

from food.models import Product


def list_products() -> QuerySet[Product]:
    return Product.objects.all()


def create_product(data: dict[str, float | bool], user: User) -> Product:
    print(data)
    if data.get("proteins_per_100_g") >= 15:
        data["is_high_protein"] = True

    if data.get("sugar_per_100_g") <= 5:
        data["is_low_sugar"] = True

    if user.is_staff:
        return Product.objects.create(**data, is_verified=True)
    else:
        return Product.objects.create(**data)
