from django.contrib import admin
from .models import Recipe
@admin.register(Recipe)
class RecipeModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','image','serves','time','ingredients','steps']

