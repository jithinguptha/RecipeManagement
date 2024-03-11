from django.contrib import admin
from django.contrib.admin import register

from recipes.models import Recipes

from recipes.models import Reviews

# Register your models here.

admin.site.register(Recipes)
admin.site.register(Reviews)

