# Generated by Django 3.2 on 2021-08-26 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tallaC',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='tallaG',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='tallaM',
            field=models.IntegerField(default=1),
        ),
    ]
