# Generated by Django 3.1.2 on 2020-10-17 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.DateField(),
        ),
    ]