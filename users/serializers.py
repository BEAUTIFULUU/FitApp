from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers
from users.validators import validate_user_birth_date
from users.choices import ACTIVITY_CHOICES, GOAL_CHOICES
from users.models import UserProfile
from users.services import calculate_user_age


class UserProfileInputSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=1, max_length=60)
    surname = serializers.CharField(min_length=1, max_length=60)
    birth_date = serializers.DateField(validators=[validate_user_birth_date])
    weight = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(20), MaxValueValidator(800)],
    )
    height = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(100), MaxValueValidator(300)],
    )
    activity = serializers.ChoiceField(choices=ACTIVITY_CHOICES)
    goal = serializers.ChoiceField(choices=GOAL_CHOICES)


class UserProfileOutputSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    height = serializers.SerializerMethodField()
    weight = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = [
            "name",
            "surname",
            "weight",
            "height",
            "activity",
            "age",
            "goal",
        ]

    def get_age(self, obj: UserProfile):
        return calculate_user_age(birth_date=obj.birth_date)

    def get_height(self, obj: UserProfile):
        return f"{obj.height} cm"

    def get_weight(self, obj: UserProfile):
        return f"{obj.weight} kg"
