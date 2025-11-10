from django import forms
from django.core.exceptions import ValidationError
from .models import Product

FORBIDDEN_WORDS = {
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар',
}


def _validate_forbidden(text: str, field_verbose: str):
    if not text:
        return
    lowered = text.lower()
    bad = [w for w in FORBIDDEN_WORDS if w in lowered]
    if bad:
        raise ValidationError(
            f"Поле «{field_verbose}» содержит запрещённые слова: {', '.join(sorted(bad))}."
        )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        # Поле "Название"
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название товара'
        })

        # Настройка атрибутов виджета для поля "Описание"
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание товара (без запрещённых слов)',
            'rows': 4
        })

        # Настройка атрибутов виджета для поля "Цена"
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену товара',
            'min': '0',
            'step': '0.01',
            'type': 'number'
        })

        # Настройка атрибутов виджета для поля "Категория"
        self.fields['category'].widget.attrs.update({
            'class': 'form-select'
        })

        # Настройка атрибутов виджета для поля "Изображение"
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'accept': 'image/*'
        })

    def clean_name(self):
        value = self.cleaned_data.get('name')
        _validate_forbidden(value, 'Название')
        return value

    def clean_description(self):
        value = self.cleaned_data.get('description')
        _validate_forbidden(value, 'Описание')
        return value

    def clean_price(self):
        value = self.cleaned_data.get('price')
        if value is not None and value < 0:
            raise ValidationError("Цена не может быть отрицательной.")
        return value
