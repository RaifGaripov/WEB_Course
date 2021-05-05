from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import  reverse_lazy
from .models import Podcast, Like, Listen
from .forms import PodcastForm, CategoryForm
from django.contrib.auth.decorators import login_required
from .filters import PodcastFilter



class home_view(ListView):
    model = Podcast
    template_name = 'main/view.html'

class detail_view(DetailView):
    model = Podcast
    template_name = 'main/details.html'

class update_view(UpdateView):
    model = Podcast
    template_name = 'main/update.html'
    fields = ["title", "descript", "author", "category",
              "file", "duration", "image"]
class delete_view(DeleteView):
    model = Podcast
    template_name = 'main/delete.html'
    success_url = reverse_lazy('home')

def index(request):
    podcasts = Podcast.objects.all().order_by('-id')[:5]
    like_podcasts = Podcast.objects.all().order_by('-likes')
    listen_podcasts = Podcast.objects.all().order_by('-listened')
    return render(request, 'main/index.html',
                  {'title': 'Главная страница сайта', 'podcasts': podcasts,
                   'like_podcasts': like_podcasts, 'listen_podcasts': listen_podcasts})

def search(request):
    podcasts = Podcast.objects.all().order_by('-id')[:5]
    myFilter = PodcastFilter(request.GET, queryset=podcasts)
    podcasts = myFilter.qs
    context = {'myFilter': myFilter, 'podcasts': podcasts}
    return render(request, 'main/about.html', context)

def create(request):
    #save podcast
    error = ""
    form = PodcastForm()
    if request.method == "POST":
        form = PodcastForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = form.errors
    context = {
        "form": form,
        "error": error
    }
    return render(request, 'main/create.html', context)

def category(request):
    error = ""
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = form.errors
    context = {
        "form": form,
        "error": error}
    return render(request, 'main/category.html', context)

@login_required
def listen_podcast(request):
    user = request.user
    if request.method == 'POST':
        podcast_id = request.POST.get('podcast_id')
        podcast_obj = Podcast.objects.get(id=podcast_id)

        if user not in podcast_obj.listened.all():
            podcast_obj.listened.add(user)

            listen, created = Listen.objects.get_or_create(user=user, podcast_id=podcast_id)

            if not created:
                if listen.value == 'Listened':
                    listen.value = 'Unlistened'
                else:
                    listen.value = 'Listened'
            else:
                listen.value = 'Listened'

                podcast_obj.save()
                listen.save()

    return redirect('home')

@login_required
def like_unlike_podcast(request):
    user = request.user
    if request.method == 'POST':
        podcast_id = request.POST.get('podcast_id')
        podcast_obj = Podcast.objects.get(id=podcast_id)


        if user in podcast_obj.likes.all():
            podcast_obj.likes.remove(user)
        else:
            podcast_obj.likes.add(user)

        like, created = Like.objects.get_or_create(user=user, podcast_id=podcast_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        else:
            like.value = 'Like'

            podcast_obj.save()
            like.save()

    return redirect('home')
