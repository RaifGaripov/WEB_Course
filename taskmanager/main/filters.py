import django_filters
from .models import*

class PodcastFilter(django_filters.FilterSet):
    class Meta:
        model = Podcast
        fields = '__all__'
        exclude = ['file', 'image', 'descript', 'listened', 'likes']