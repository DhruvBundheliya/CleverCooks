from django.contrib import admin
from .models import Recipe, Newsletter
admin.site.register(Newsletter)
@admin.register(Recipe)
class RecipeModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','coverImage','serves','time','ingredients','instructions']

