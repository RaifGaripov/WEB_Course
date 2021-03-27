from .models import Podcast
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