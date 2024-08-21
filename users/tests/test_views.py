from datetime import date
from decimal import Decimal

import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from users.models import UserProfile


@pytest.fixture
def authenticated_user() -> User:
    user = User.objects.create_user(username="testuser123", password="testpassword123")
    return user


@pytest.fixture
def api_client(authenticated_user: User) -> APIClient:
    client = APIClient()
    client.force_login(authenticated_user)
    return client


@pytest.fixture
def user_profile(authenticated_user: User) -> UserProfile:
    return UserProfile.objects.create(
        name="testname",
        surname="testsurname",
        weight=Decimal(80),
        height=Decimal(185),
        activity="1-2 times per week",
        birth_date=date(day=2, month=6, year=2001),
        goal="Gain weight",
        user=authenticated_user,
    )


@pytest.mark.django_db
class TestUserProfileDetailView:
    def test_user_profile_detail_view_return_403_for_anonymous_user(self):
        client = APIClient()
        url = "user_details"
        response = client.get(reverse(url))
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_user_profile_detail_view_return_200_and_created_profile_for_authenticated_user_with_no_profile(
        self, api_client: APIClient, authenticated_user: User
    ):
        url = "user_details"
        response = api_client.get(reverse(url))
        assert response.status_code == status.HTTP_200_OK
        created_profile = UserProfile.objects.get(user=authenticated_user)
        expected_data = {
            "name": created_profile.name,
            "surname": created_profile.surname,
            "weight": f"{created_profile.weight} kg",
            "height": f"{created_profile.height} cm",
            "activity": created_profile.activity,
            "age": None,
            "goal": created_profile.goal,
        }
        assert response.data == expected_data

    def test_user_profile_detail_view_return_200_and_profile_for_authenticated_user_with_profile(
        self, api_client: APIClient, user_profile: UserProfile
    ):
        url = "user_details"
        response = api_client.get(reverse(url))
        assert response.status_code == status.HTTP_200_OK
        retrieved_profile = UserProfile.objects.get(user=user_profile.user)
        expected_data = {
            "name": retrieved_profile.name,
            "surname": retrieved_profile.surname,
            "weight": f"{retrieved_profile.weight} kg",
            "height": f"{retrieved_profile.height} cm",
            "activity": retrieved_profile.activity,
            "age": 23,
            "goal": retrieved_profile.goal,
        }
        assert response.data == expected_data

    def test_user_profile_detail_view_return_200_for_authenticated_user_if_profile_updated(
        self, api_client: APIClient, user_profile: UserProfile
    ):
        url = "user_details"
        data = {
            "name": "changedname",
            "surname": "changedsurname",
            "goal": "Lose weight",
        }
        response = api_client.put(reverse(url), data=data)
        assert response.status_code == status.HTTP_200_OK
        for key, value in data.items():
            assert response.data[key] == value

    def test_user_profile_detail_view_return_204_for_authenticated_user_if_profile_deleted(
        self, api_client: APIClient, user_profile: UserProfile
    ):
        url = "user_details"
        response = api_client.delete(reverse(url))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert UserProfile.objects.filter(id=user_profile.id).count() == 0
