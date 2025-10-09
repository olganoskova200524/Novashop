# Novashop

Учебный проект интернет-магазина на Django.  
Проект будет развиваться на протяжении курса: от базовой структуры до полноценного приложения с каталогом, корзиной и оформлением заказов.

## Технологии
- Python 3.12
- Django
- Poetry

## Приложения
- `catalog` — управление товарами

## Установка
```bash
poetry install
poetry run python manage.py migrate
poetry run python manage.py runserver

