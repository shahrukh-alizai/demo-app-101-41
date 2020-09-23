# Generated by Django 2.2.16 on 2020-09-23 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_demo_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="new_field",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="homepage_new_field",
                to="home.Demo",
            ),
        ),
    ]
