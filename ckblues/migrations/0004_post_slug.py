# Generated by Django 3.1.4 on 2021-03-13 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ckblues', '0003_auto_20210313_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
