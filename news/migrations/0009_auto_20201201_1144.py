# Generated by Django 3.1.2 on 2020-12-01 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20201201_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
