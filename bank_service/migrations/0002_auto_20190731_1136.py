# Generated by Django 2.2.3 on 2019-07-31 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banks',
            options={'managed': False, 'verbose_name': 'Bank', 'verbose_name_plural': 'Banks'},
        ),
        migrations.AlterModelOptions(
            name='branches',
            options={'managed': False, 'verbose_name': 'Bank Branch', 'verbose_name_plural': 'Bank Branches'},
        ),
    ]
