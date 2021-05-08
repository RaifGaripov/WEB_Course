from django.urls import path
from django.contrib import admin

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('search', views.search, name='search'),
    path('create', views.create, name='create'),
    path('view', views.view, name='view'),
    path('like/', views.like_unlike_podcast, name='like-podcast-view'),
    path('listen/', views.listen_podcast, name='listen-view'),
    path('create/category', views.category, name='create-category'),
    path('categories', views.categories, name='categories'),
    path('details/<int:pk>', views.detail_view.as_view(), name='details'),
    path('details/update/<int:pk>', views.update_view.as_view(), name='update'),
    path('details/<int:pk>/delete', views.delete_view.as_view(), name='delete'),
]
