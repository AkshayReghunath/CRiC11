# Generated by Django 2.1.5 on 2019-02-01 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRiC11', '0004_auto_20190201_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balltype',
            name='BBI',
            field=models.CharField(max_length=8, verbose_name='Best Bowling'),
        ),
        migrations.AlterField(
            model_name='balltype',
            name='BBM',
            field=models.CharField(max_length=8, verbose_name='Best Bowling Match'),
        ),
    ]