from typing import Type
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from users.serializers import CustomUserInputSerializer, CustomUserOutputSerializer
from users.models import CustomUser
from users.services import get_custom_user_details, update_custom_user_details


class CustomUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    def get_serializer_class(
        self,
    ) -> Type[CustomUserOutputSerializer | CustomUserInputSerializer]:
        return (
            CustomUserOutputSerializer
            if self.request.method == "GET"
            else CustomUserInputSerializer
        )

    def get_object(self) -> CustomUser:
        return get_custom_user_details(user_id=self.request.user.pk)

    def update(self, request: Request, *args, **kwargs) -> Response:
        custom_user_obj = self.get_object()
        serializer = self.get_serializer(instance=custom_user_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        update_custom_user_details(data=serializer.validated_data, user=custom_user_obj)
        output_serializer = CustomUserOutputSerializer(custom_user_obj)
        return Response(output_serializer.data, status=status.HTTP_200_OK)
