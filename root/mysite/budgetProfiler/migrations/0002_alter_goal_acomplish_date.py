# Generated by Django 3.2.7 on 2021-09-28 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgetProfiler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='acomplish_date',
            field=models.DateField(verbose_name='completion date'),
        ),
    ]
