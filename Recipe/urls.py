from django.urls import path,include
from Recipe import views
urlpatterns = [
    path('',views.index,name='index'),
    path('postrecipe',views.postrecipe,name='postrecipe'),
    path('recipes',views.recipes,name='recipes'),
    path('recipe_desc',views.recipe_desc,name='recipe_desc')
]