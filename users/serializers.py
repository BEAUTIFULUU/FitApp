from rest_framework import serializers
from validators import validate_user_birth_date
from choices import ACTIVITY_CHOICES
from models import CustomUser
from services import calculate_user_age


class CustomUserInputSerializer(serializers.Serializer):
    birth_date = serializers.DateField(validators=validate_user_birth_date)
    weight = serializers.DecimalField(max_digits=3, decimal_places=2)
    height = serializers.DecimalField(max_digits=3, decimal_places=2)
    activity = serializers.ChoiceField(choices=ACTIVITY_CHOICES)


class CustomUserOutputSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField(allow_null=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'birth_date', 'weight', 'height', 'activity', 'age']

    def get_age(self, obj):
        return calculate_user_age(birth_date=obj.birth_date)
