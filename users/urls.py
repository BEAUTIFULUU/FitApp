from django.urls import path
from users.views import CustomUserDetailView

urlpatterns = [path("me/", CustomUserDetailView.as_view(), name="user_details")]
