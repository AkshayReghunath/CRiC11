# Generated by Django 2.1.5 on 2019-01-22 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ball',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('M', models.IntegerField(max_length=20, verbose_name='Matches')),
                ('Inn', models.IntegerField(max_length=20, verbose_name='Innings')),
                ('B', models.IntegerField(max_length=20, verbose_name='Balls')),
                ('Runs', models.IntegerField(max_length=20, verbose_name='Runs')),
                ('Wkts', models.IntegerField(max_length=20, verbose_name='Wickets')),
                ('BBI', models.IntegerField(max_length=20, verbose_name='Best Bowling')),
                ('BBM', models.IntegerField(max_length=20, verbose_name='Best Bowling Match')),
                ('Econ', models.IntegerField(max_length=20, verbose_name='Economy')),
                ('Avg', models.IntegerField(max_length=20, verbose_name='Average')),
                ('SR', models.IntegerField(max_length=20, verbose_name='Strike Rate')),
                ('fwh', models.IntegerField(max_length=20, verbose_name='Fife wicket')),
                ('twh', models.IntegerField(max_length=20, verbose_name='Ten wicket')),
            ],
        ),
        migrations.CreateModel(
            name='Bat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('M', models.IntegerField(max_length=20, verbose_name='Matches')),
                ('Inn', models.IntegerField(max_length=20, verbose_name='Innings')),
                ('NO', models.IntegerField(max_length=20, verbose_name='Not out')),
                ('Runs', models.IntegerField(max_length=20, verbose_name='Runs')),
                ('HS', models.IntegerField(max_length=20, verbose_name='High Score')),
                ('Avg', models.IntegerField(max_length=20, verbose_name='Average')),
                ('BF', models.IntegerField(max_length=20, verbose_name='Balls Faced')),
                ('SR', models.IntegerField(max_length=20, verbose_name='Strike Rate')),
                ('century', models.IntegerField(max_length=20, verbose_name='Century')),
                ('double', models.IntegerField(max_length=20, verbose_name='Double Century')),
                ('fifty', models.IntegerField(max_length=20, verbose_name='Fifty')),
                ('fours', models.IntegerField(max_length=20, verbose_name='Fours')),
                ('sixes', models.IntegerField(max_length=20, verbose_name='Sixes')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='NAME')),
                ('born', models.IntegerField(max_length=20, verbose_name='Matches')),
                ('birth', models.IntegerField(max_length=20, verbose_name='Matches')),
                ('role', models.IntegerField(max_length=20, verbose_name='Matches')),
                ('batstyle', models.IntegerField(max_length=20, verbose_name='Matches')),
                ('ballstyle', models.IntegerField(max_length=20, verbose_name='Matches')),
                ('p', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='CRiC11.Ball')),
            ],
        ),
    ]
