# Generated by Django 3.1.2 on 2020-10-16 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0004_auto_20201017_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meals',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
