# Generated by Django 4.2.2 on 2023-08-05 15:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("functions", "0004_function_runtime"),
    ]

    operations = [
        migrations.AlterField(
            model_name="function",
            name="runtime",
            field=models.CharField(max_length=20),
        ),
    ]
