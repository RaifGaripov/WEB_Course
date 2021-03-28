from django.db import models
#from django.contrib.auth.models import User

class Podcast(models.Model):
    title = models.CharField('Название', max_length=50)
    descript = models.TextField('Описание')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Подкасты'
        verbose_name_plural = 'Подкаст'

'''class UserModel(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField('Биография')

    def __str__(self):
        return str(self.user)
'''