# Generated by Django 4.2.6 on 2023-11-27 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='dish_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
