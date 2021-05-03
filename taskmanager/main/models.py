from django.db import models
from django.contrib.auth.models import User
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
    file = models.FileField(null=True, blank=True, upload_to='media/audio/')
    duration = models.FloatField(default=0)
    image = models.ImageField(null=True, blank=True, upload_to='media/img/')
    listened = models.ManyToManyField(User, related_name='listened', default=None, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', default=None, blank=True)

    def __str__(self):
        return self.title + ' + ' + self.author

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name = 'Подкаст'
        verbose_name_plural = 'Подкасты'


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.podcast}-{self.value}"

LISTEN_CHOICES = (
    ('Listened', 'Listened'),
    ('Unlistened', 'Unlistened'),
)


class Listen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    value = models.CharField(choices=LISTEN_CHOICES, max_length=15)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.podcast}-{self.value}"
