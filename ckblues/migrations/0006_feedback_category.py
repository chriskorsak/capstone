# Generated by Django 3.1.4 on 2021-03-24 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ckblues', '0005_auto_20210323_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='category',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]