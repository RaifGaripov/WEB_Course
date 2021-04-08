from django.contrib import admin
from .models import Podcast, Category#, UserModel

admin.site.register(Podcast)
admin.site.register(Category)
#admin.site.register(UserModel)