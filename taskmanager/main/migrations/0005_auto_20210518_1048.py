# Generated by Django 3.1.7 on 2021-05-18 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_podcast_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='author',
            field=models.CharField(default='Неизвестен', max_length=50, verbose_name='Автор'),
        ),
    ]
