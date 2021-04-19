# Generated by Django 3.1.7 on 2021-04-17 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210409_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='file',
            field=models.FileField(blank=True, upload_to='media/audio'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/img'),
        ),
    ]
