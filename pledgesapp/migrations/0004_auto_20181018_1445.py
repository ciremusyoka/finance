# Generated by Django 2.1.2 on 2018-10-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pledgesapp', '0003_auto_20181018_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allpledges',
            name='amount_paid',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=1000000, null=True),
        ),
        migrations.AlterField(
            model_name='allpledges',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=1000000, null=True),
        ),
    ]
