# Generated by Django 2.1.2 on 2018-10-18 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmanager', '0003_auto_20181018_1344'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agmbalances',
            options={'verbose_name_plural': 'AGM balances'},
        ),
        migrations.AlterModelOptions(
            name='agmcontributions',
            options={'verbose_name_plural': 'AGM  payments'},
        ),
        migrations.AlterModelOptions(
            name='members',
            options={'verbose_name_plural': 'Members'},
        ),
    ]