from .models import Podcast, Category#, UserModel
from django import forms


class PodcastForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = ["title", "descript", "author", "category",
                  "file", "duration", "image"]
        category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                          to_field_name='Выберите категорию'),
        file = forms.FileField(required=False)
        image = forms.FileField(required=False)
        duration = forms.FloatField()

        widgets = {
            "title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "author": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите автора'
            }),
            "descript": forms.Textarea(attrs={
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