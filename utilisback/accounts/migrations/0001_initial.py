# Generated by Django 3.0.2 on 2020-01-16 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email_address', models.CharField(max_length=25)),
                ('wallet_address', models.CharField(max_length=25)),
                ('country_of_origin', models.CharField(max_length=25)),
                ('id_number', models.CharField(max_length=25)),
            ],
        ),
    ]
