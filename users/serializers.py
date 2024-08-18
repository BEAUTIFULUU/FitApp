from rest_framework import serializers
from users.validators import validate_user_birth_date
from users.choices import ACTIVITY_CHOICES
from users.models import CustomUser
from users.services import calculate_user_age


class CustomUserInputSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=1, max_length=60)
    surname = serializers.CharField(min_length=1, max_length=60)
    birth_date = serializers.DateField(validators=[validate_user_birth_date])
    weight = serializers.DecimalField(max_digits=5, decimal_places=2)
    height = serializers.DecimalField(max_digits=5, decimal_places=2)
    activity = serializers.ChoiceField(choices=ACTIVITY_CHOICES)


class CustomUserOutputSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField(allow_null=True)

    class Meta:
        model = CustomUser
        fields = [
            "name",
            "surname",
            "birth_date",
            "weight",
            "height",
            "activity",
            "age",
        ]

    def get_age(self, obj):
        return calculate_user_age(birth_date=obj.birth_date)
