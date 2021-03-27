from django.shortcuts import render, redirect
from .models import Podcast
from .forms import PodcastForm

def index(request):
    podcasts = Podcast.objects.all()
    sorted_podcasts = Podcast.objects.order_by('-id')[:5] #last top 5
    return render(request, 'main/index.html',
                  {'title': 'Главная страница сайта', 'podcasts': podcasts})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    #save podcast
    error = ""
    form = PodcastForm()
    if request.method == "POST":
        form = PodcastForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма была неверной"
    context = {
        "form": form,
        "error": error
    }
    return render(request, 'main/create.html', context)
