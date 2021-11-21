from django.contrib import admin
from .models import Recipe
@admin.register(Recipe)
class RecipeModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','coverImage','serves','time','ingredients','instructions']

