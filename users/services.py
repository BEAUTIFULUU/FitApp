import uuid
from datetime import date

from rest_framework.generics import get_object_or_404

from users.models import CustomUser


def calculate_user_age(birth_date: date) -> int | None:
    if birth_date is None:
        return None

    today = date.today()
    age = (
        today.year
        - birth_date.year
        - ((today.month, today.day) < (birth_date.month, birth_date.day))
    )
    return age


def get_custom_user_details(user_id: uuid.UUID) -> CustomUser:
    return get_object_or_404(CustomUser, id=user_id)


def update_custom_user_details(data: dict[str, str | float], user: CustomUser) -> None:
    for key, value in data.items():
        setattr(user, key, value)
    user.save()
