from datetime import date
from django.contrib.auth.models import User
from users.models import UserProfile


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


def get_or_create_user_profile(user: User) -> UserProfile:
    profile, created = UserProfile.objects.get_or_create(user=user)
    return profile


def update_user_profile_details(
    data: dict[str, str | float], user_profile: UserProfile
) -> None:
    for key, value in data.items():
        setattr(user_profile, key, value)
    user_profile.save()
