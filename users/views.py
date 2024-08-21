from typing import Type
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from users.serializers import UserProfileInputSerializer, UserProfileOutputSerializer
from users.models import UserProfile
from users.services import get_or_create_user_profile, update_user_profile_details


class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    def get_serializer_class(
        self,
    ) -> Type[UserProfileOutputSerializer | UserProfileInputSerializer]:
        return (
            UserProfileOutputSerializer
            if self.request.method == "GET"
            else UserProfileInputSerializer
        )

    def get_object(self) -> UserProfile:
        return get_or_create_user_profile(user=self.request.user)

    def update(self, request: Request, *args, **kwargs) -> Response:
        custom_user_obj = self.get_object()
        serializer = self.get_serializer(
            instance=custom_user_obj, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        update_user_profile_details(
            data=serializer.validated_data, user_profile=custom_user_obj
        )
        output_serializer = UserProfileOutputSerializer(custom_user_obj)
        return Response(output_serializer.data, status=status.HTTP_200_OK)
