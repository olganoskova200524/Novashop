from pathlib import Path
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection, transaction
from catalog.models import Product, Category

class Command(BaseCommand):
    help = "Очистить БД и загрузить тестовые данные из catalog/fixtures/catalog_fixture.json"

    def add_arguments(self, parser):
        parser.add_argument(
            "--hard",
            action="store_true",
            help="PostgreSQL: TRUNCATE + RESTART IDENTITY (обнуляет ID). Иначе delete() через ORM.",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        fixtures_path = Path(__file__).resolve().parent.parent.parent / "fixtures" / "catalog_fixture.json"

        # очистка данных (сначала продукты -> FK на категории)
        if options["hard"] and connection.vendor == "postgresql":
            with connection.cursor() as cur:
                cur.execute('TRUNCATE TABLE "catalog_product","catalog_category" RESTART IDENTITY CASCADE;')
            self.stdout.write(self.style.WARNING("TRUNCATE выполнен (ID сброшены)."))
        else:
            Product.objects.all().delete()
            Category.objects.all().delete()
            self.stdout.write(self.style.WARNING("Удаление через ORM (ID могут не сброситься)."))

        # проверка наличия фикстуры
        if not fixtures_path.exists():
            self.stderr.write(f"Не найден файл фикстуры: {fixtures_path}")
            return

        # загрузка фикстуры
        call_command("loaddata", str(fixtures_path))

        self.stdout.write(self.style.SUCCESS("Данные загружены из catalog_fixture.json"))
