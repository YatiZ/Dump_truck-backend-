# Generated by Django 4.1 on 2023-03-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car_app", "0006_alter_order_deleted_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customerinfo",
            name="deleted_at",
            field=models.DateField(null=True),
        ),
    ]
