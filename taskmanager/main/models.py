from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from django.urls import reverse
class Category(models.Model):
    name = models.CharField('Название', max_length=50)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name




class Podcast(models.Model):
    title = models.CharField('Название', max_length=50)
    descript = models.TextField('Описание')
    author = models.TextField('Автор', max_length=50, default='Неизвестен')

    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

    post_date = models.DateField(null=True, auto_now_add=True)
    file = models.FileField(blank=True)
    duration = models.FloatField(default=0)
    image = models.ImageField(upload_to='podcasts', blank=True)
    listened = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title + ' + ' + self.author

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name = 'Подкаст'
        verbose_name_plural = 'Подкасты'

'''class UserModel(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField('Биография')

    def __str__(self):
        return str(self.user)
'''