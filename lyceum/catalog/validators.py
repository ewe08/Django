import re
from functools import wraps

from django.core.exceptions import ValidationError


def validate_must_be_param(*args):
    @wraps(validate_must_be_param)
    def word_validate(value):
        must_be_in_our_item = set(args)
        value = re.sub(" +", " ", value)
        no_html_value = re.sub(r'(\<(/?[^>]+)>)', '', value)
        cleaned_value = re.sub(r'[^\w\s]', '', no_html_value)
        cleaned_value = set(cleaned_value.lower().split())
        if not (cleaned_value & must_be_in_our_item):
            raise ValidationError(
                f'Обязательно должны быть слова: '
                f'{" ".join(list(must_be_in_our_item))}')

        return value
    return word_validate
