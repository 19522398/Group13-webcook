# Generated by Django 4.2.5 on 2023-10-01 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_alter_recipe_recipe_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_url',
        ),
    ]
