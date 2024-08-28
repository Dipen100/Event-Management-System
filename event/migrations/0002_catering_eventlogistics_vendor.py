# Generated by Django 5.0.4 on 2024-08-28 07:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("event", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Catering",
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
                ("name", models.CharField(max_length=30)),
                ("address", models.CharField(max_length=50)),
                ("phone", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="EventLogistics",
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
                ("equipments", models.CharField(max_length=100)),
                (
                    "transportation",
                    models.CharField(
                        choices=[
                            ("BUS", "B"),
                            ("CAR", "C"),
                            ("VAN", "V"),
                            ("SCORPIO", "S"),
                        ],
                        max_length=9,
                    ),
                ),
                (
                    "catering",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="event.catering"
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="event.event"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Vendor",
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
                ("name", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("address", models.CharField(max_length=30)),
                ("phone", models.IntegerField()),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="event.event"
                    ),
                ),
            ],
        ),
    ]
