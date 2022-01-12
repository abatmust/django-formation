from typing import Any
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from account.models import Profile


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "email", "username", "password1", "password2")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "email", "username",
                  "bio", "github_link", "linkdin_link"]

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
