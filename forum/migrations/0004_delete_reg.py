# Generated by Django 4.0.6 on 2022-08-29 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_reg'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reg',
        ),
    ]