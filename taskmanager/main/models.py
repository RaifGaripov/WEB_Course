from django.db import models

class Podcast(models.Model):
    title = models.CharField('Название', max_length=50)
    descript = models.TextField('Описание')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Подкасты'
        verbose_name_plural = 'Подкаст'