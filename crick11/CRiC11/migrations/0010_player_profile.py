# Generated by Django 2.1.5 on 2019-02-02 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRiC11', '0009_auto_20190201_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='profile',
            field=models.CharField(max_length=30000, null=True, verbose_name='Ball Style'),
        ),
    ]
