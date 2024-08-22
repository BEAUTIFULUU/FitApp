from django.urls import path
from users.views import UserProfileDetailView

urlpatterns = [
    path("user_profile/", UserProfileDetailView.as_view(), name="user_details")
]
