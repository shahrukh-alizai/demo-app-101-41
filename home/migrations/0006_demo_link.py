# Generated by Django 2.2.16 on 2020-09-23 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='demo',
            name='link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demo_link', to='home.CustomText'),
        ),
    ]