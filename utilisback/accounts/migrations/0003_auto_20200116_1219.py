# Generated by Django 3.0.2 on 2020-01-16 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200116_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='email_address',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='id_number',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='members',
            name='wallet_address',
            field=models.CharField(max_length=64),
        ),
    ]