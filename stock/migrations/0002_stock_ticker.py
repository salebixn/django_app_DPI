# Generated by Django 4.1.4 on 2022-12-27 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='ticker',
            field=models.CharField(default='NULL', max_length=4),
        ),
    ]
