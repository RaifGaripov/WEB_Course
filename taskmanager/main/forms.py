from .models import Podcast, Category
from django import forms


class PodcastForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = ["title", "descript", "author", "category",
                  "file", "duration", "image"]

        widgets = {
            "title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
           "descript": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "author": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите автора'
            }),
        }
        category = forms.ModelChoiceField(
            queryset=Category.objects.all(),
            to_field_name='Выберите категорию', help_text="Выберите категорию")

        duration = forms.FloatField()
        file = forms.FileField(required=False)
        image = forms.ImageField(required=False)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            })
        }