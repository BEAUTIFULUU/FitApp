from datetime import date


def calculate_user_age(birth_date: date) -> int | None:
    if birth_date is None:
        return None

    today = date.today()
    age = (
            today.year
            - birth_date.year
            - ((today.month, today.day) < (birth_date.month, birth_date.day))
    )
    return age
