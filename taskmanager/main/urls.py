from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('search', views.search, name='search'),
    path('create', views.create, name='create'),
    path('view', views.home_view.as_view(), name='view'),
    path('details/<int:pk>', views.detail_view.as_view(), name='details'),
    path('details/update/<int:pk>', views.update_view.as_view(), name='update'),
    path('details/<int:pk>/delete', views.delete_view.as_view(), name='delete'),
    path('like/', views.like_unlike_podcast, name='like-podcast-view'),
    path('listen/', views.listen_podcast, name='listen-view'),
    path('create/category', views.category, name='category'),
]
