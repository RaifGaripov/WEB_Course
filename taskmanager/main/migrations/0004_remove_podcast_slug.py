# Generated by Django 3.1.7 on 2021-04-29 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_listen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='podcast',
            name='slug',
        ),
    ]
