# Generated by Django 2.2.16 on 2020-09-10 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_load_initial_data"),
    ]

    operations = [
        migrations.CreateModel(
            name="Demo",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
            ],
            options={
                "verbose_name_plural": "Custom Demo verbose",
            },
        ),
    ]
