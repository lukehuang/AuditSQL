# Generated by Django 2.0.2 on 2018-05-28 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mstats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysqlquerylog',
            name='affect_rows',
            field=models.IntegerField(default=0, verbose_name='影响行数'),
        ),
    ]
