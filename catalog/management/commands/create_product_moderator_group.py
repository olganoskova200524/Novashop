from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from catalog.models import Product


class Command(BaseCommand):
    help = "Создаёт группу 'Модератор продуктов' с нужными правами"

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name="Модератор продуктов")

        product_ct = ContentType.objects.get_for_model(Product)

        # кастомное право can_unpublish_product
        unpublish_perm = Permission.objects.get(
            codename="can_unpublish_product",
            content_type=product_ct,
        )

        # стандартное право удаления продукта
        delete_perm = Permission.objects.get(
            codename="delete_product",
            content_type=product_ct,
        )

        group.permissions.add(unpublish_perm, delete_perm)

        self.stdout.write(
            self.style.SUCCESS(
                "Группа 'Модератор продуктов' успешно создана или обновлена."
            )
        )
