# Generated by Django 3.1.2 on 2020-10-16 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0005_auto_20201017_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
