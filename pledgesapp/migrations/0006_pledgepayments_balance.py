# Generated by Django 2.1.2 on 2018-10-18 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pledgesapp', '0005_allpledges_initial_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledgepayments',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=1000000),
            preserve_default=False,
        ),
    ]
