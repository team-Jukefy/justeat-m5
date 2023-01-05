# Generated by Django 4.1.5 on 2023-01-05 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Menu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("drinks", "Drinks"),
                            ("foods", "Foods"),
                            ("disserts", "Disserts"),
                        ],
                        max_length=8,
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                ("description", models.CharField(max_length=250)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
    ]