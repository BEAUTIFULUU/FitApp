from datetime import date, timedelta
import pytest
from rest_framework.exceptions import ValidationError
from users.validators import validate_user_birth_date


def test_validate_user_birth_date_raise_error_if_date_in_future():
    with pytest.raises(ValidationError) as error:
        validate_user_birth_date(birth_date=date.today() + timedelta(days=1))
        assert error.value == "Birth date cannot be in the future."
