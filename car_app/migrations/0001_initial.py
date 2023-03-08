# Generated by Django 4.1 on 2023-03-07 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CarInfo",
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
                ("car_no", models.TextField(max_length=50)),
                ("maintenance", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="CustomerInfo",
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
                ("customer_name", models.CharField(max_length=200)),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now_add=True)),
                ("deleted_at", models.DateField(auto_now_add=True)),
                ("phone_no", models.TextField(blank=True, max_length=50)),
                ("address", models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now_add=True)),
                ("deleted_at", models.DateField(auto_now_add=True)),
                ("count", models.IntegerField(blank=True)),
                (
                    "service_fees_per_count",
                    models.TextField(blank=True, max_length=100),
                ),
                ("debt_amount", models.TextField(blank=True, max_length=100)),
                ("description", models.TextField(blank=True, max_length=200)),
                ("paid_amount", models.TextField(blank=True, max_length=100)),
                (
                    "car_id",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="car_app.carinfo",
                    ),
                ),
                (
                    "customer_id",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="car_app.customerinfo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Investment",
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
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now_add=True)),
                ("deleted_at", models.DateField(auto_now_add=True)),
                ("petrol", models.TextField(blank=True)),
                ("driver_fees", models.TextField()),
                ("extra_cost", models.TextField(blank=True)),
                ("cost_for_home", models.TextField()),
                (
                    "car_id",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="car_app.carinfo",
                    ),
                ),
            ],
        ),
    ]