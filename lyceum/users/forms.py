from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Custom form for creating new user."""

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    """Custom form for changing user data."""

    password = None

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'birthday')
