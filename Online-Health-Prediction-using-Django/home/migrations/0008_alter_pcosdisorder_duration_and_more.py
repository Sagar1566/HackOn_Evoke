# Generated by Django 5.0.2 on 2024-03-26 14:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0007_pcosdisorder"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pcosdisorder",
            name="duration",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(31),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="pcosdisorder",
            name="period_frequency",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(12),
                ]
            ),
        ),
    ]
