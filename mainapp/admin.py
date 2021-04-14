from django.contrib import admin

# Register your models here.
from mainapp.models import FavoritesResume, FavoritesVacancies

admin.site.register(FavoritesResume)
admin.site.register(FavoritesVacancies)