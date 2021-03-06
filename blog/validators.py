from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_file_type(value):
    if not value.name.endswith('.md'):
        raise ValidationError('Filetype must be .md!')
    else:
        return value
