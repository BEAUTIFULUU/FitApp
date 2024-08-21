from decimal import Decimal
from datetime import date
import pytest
from django.contrib.auth import get_user_model
from users.models import UserProfile
from users.services import (
    calculate_user_age,
    get_or_create_user_profile,
    update_user_profile_details,
)

User = get_user_model()


@pytest.fixture
def user() -> User:
    user = User.objects.create(username="testuser123", password="testpassword123")
    return user


@pytest.fixture
def user_with_profile() -> User:
    user_with_profile = User.objects.create(
        username="testuser222", password="testpassword333"
    )
    return user_with_profile


@pytest.fixture
def user_profile(user_with_profile: User) -> User:
    profile = UserProfile.objects.create(user=user_with_profile)
    return profile


@pytest.mark.django_db
class TestUsersServices:
    def test_calculate_user_age_return_correct_age(self):
        result = calculate_user_age(birth_date=date(day=2, month=6, year=2001))
        assert result == 23

    def test_get_or_create_user_profile_create_user_profile_if_profile_doesnt_exist(
        self, user: User
    ):
        assert UserProfile.objects.filter(user=user).count() == 0
        get_or_create_user_profile(user=user)
        assert UserProfile.objects.filter(user=user).count() == 1

    def test_get_or_create_user_profile_return_profile_if_profile_exists(
        self, user_profile: UserProfile
    ):
        profile = get_or_create_user_profile(user=user_profile.user)
        assert profile.user.pk == user_profile.user.pk

    def test_update_user_profile_details_correctly_updates_profile(
        self, user_profile: UserProfile
    ):
        data = {
            "name": "testname",
            "surname": "testsurname",
            "birth_date": date(day=1, month=1, year=2000),
            "weight": Decimal(85),
            "height": Decimal(185),
            "activity": "1-2 times a week",
            "goal": "Lose weight",
        }
        update_user_profile_details(data=data, user_profile=user_profile)
        for key, value in data.items():
            assert getattr(user_profile, key) == value
