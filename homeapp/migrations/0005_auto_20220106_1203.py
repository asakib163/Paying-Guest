# Generated by Django 3.1.7 on 2022-01-06 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0004_auto_20220106_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pgroombooking',
            name='homes',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pgroombooking',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]
