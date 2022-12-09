from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Custom form for creating new user."""

    class Meta(UserCreationForm):
        model = CustomUser
        fields = (CustomUser.email.field.name,)


class CustomUserChangeForm(UserChangeForm):
    """Custom form for changing user data."""

    password = None

    class Meta:
        model = CustomUser
        fields = (
            CustomUser.first_name.field.name,
            CustomUser.last_name.field.name,
            CustomUser.email.field.name,
            CustomUser.birthday.field.name,
        )
