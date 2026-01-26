from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].label = "Email"
        self.fields["first_name"].label = "Имя"
        self.fields["last_name"].label = "Фамилия"
        self.fields["password1"].label = "Пароль"
        self.fields["password2"].label = "Повторите пароль"

        self.fields["email"].widget.attrs.update({
            "placeholder": "Введите email"
        })
        self.fields["first_name"].widget.attrs.update({
            "placeholder": "Введите имя"
        })
        self.fields["last_name"].widget.attrs.update({
            "placeholder": "Введите фамилию"
        })
        self.fields["password1"].widget.attrs.update({
            "placeholder": "Введите пароль"
        })
        self.fields["password2"].widget.attrs.update({
            "placeholder": "Повторите пароль"
        })

        for field in self.fields.values():
            existing = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = (existing + " form-control").strip()


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].label = "Email"
        self.fields["username"].widget.attrs.update({"placeholder": "Введите email"})
        self.fields["password"].label = "Пароль"
        self.fields["password"].widget.attrs.update({"placeholder": "Введите пароль"})

        for field in self.fields.values():
            existing_classes = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = (existing_classes + " form-control").strip()
