from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('view', views.home_view.as_view(), name='view'),
    path('details/<int:pk>', views.detail_view.as_view(), name='details'),
]
