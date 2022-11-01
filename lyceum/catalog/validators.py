from functools import wraps

from django.core.exceptions import ValidationError


def validate_must_be_param(*args):
    @wraps(validate_must_be_param)
    def word_validate(value):
        must_be_in_our_item = set(args)

        cleaned_value = set(value.lower().split())
        if not (cleaned_value & must_be_in_our_item):
            raise ValidationError(
                f'Обязательно должны быть слова: '
                f'{" ".join(list(must_be_in_our_item))}')

        return value
    return word_validate