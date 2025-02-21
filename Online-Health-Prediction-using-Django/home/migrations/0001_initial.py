# Generated by Django 5.0.2 on 2024-03-10 19:36

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ObesityDate",
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
                ("age", models.IntegerField()),
                ("gender", models.CharField(max_length=6)),
                ("height", models.FloatField()),
                ("weight", models.FloatField()),
                ("bmi", models.FloatField()),
                ("activityLevel", models.FloatField()),
                ("ObesityCategory", models.CharField(max_length=20)),
            ],
        ),
    ]
