# Generated by Django 2.2.16 on 2020-09-23 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_title'),
        ('home', '0009_auto_20200923_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='test',
        ),
        migrations.DeleteModel(
            name='TestModel',
        ),
    ]
