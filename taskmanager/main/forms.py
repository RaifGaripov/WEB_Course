from .models import Podcast#, UserModel
from django.forms import ModelForm, TextInput, Textarea


class PodcastForm(ModelForm):
    class Meta:
        model = Podcast
        fields = ["title", "descript"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "descript": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }
'''class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ['name', 'birthday', 'email']
        widgets = {
             "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "birthday": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату рождения'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите почту'
            }),
        }'''