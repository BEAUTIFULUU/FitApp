from django.urls import path
from users.views import UserProfileDetailView

urlpatterns = [path("me/", UserProfileDetailView.as_view(), name="user_details")]
