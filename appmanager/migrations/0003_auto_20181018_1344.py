# Generated by Django 2.1.2 on 2018-10-18 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmanager', '0002_agmbalances_agmcontributions'),
    ]

    operations = [
        migrations.CreateModel(
            name='members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='agmbalances',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=1000000),
        ),
        migrations.AlterField(
            model_name='agmcontributions',
            name='amount_paid',
            field=models.DecimalField(decimal_places=2, max_digits=1000000),
        ),
    ]