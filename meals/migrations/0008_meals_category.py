# Generated by Django 3.1.2 on 2020-10-17 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0007_auto_20201017_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='meals.category'),
        ),
    ]