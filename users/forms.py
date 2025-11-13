from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].label = "Email"
        self.fields["password1"].label = "Пароль"
        self.fields["password2"].label = "Повторите пароль"

        self.fields["email"].widget.attrs.update({"placeholder": "Введите email"})
        self.fields["password1"].widget.attrs.update({"placeholder": "Введите пароль"})
        self.fields["password2"].widget.attrs.update({"placeholder": "Повторите пароль"})


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].label = "Email"
        self.fields["username"].widget.attrs.update({"placeholder": "Введите email"})
        self.fields["password"].label = "Пароль"
        self.fields["password"].widget.attrs.update({"placeholder": "Введите пароль"})
