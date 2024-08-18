from datetime import date
from rest_framework.exceptions import ValidationError


def validate_user_birth_date(birth_date: date) -> None:
    if birth_date > date.today():
        raise ValidationError("Birth date cannot be in the future.")
