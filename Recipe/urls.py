from django.urls import path,include
from Recipe import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('postrecipe',views.postrecipe,name='postrecipe'),
    path('recipes',views.recipes,name='recipes'),
    path('recipe_desc',views.recipe_desc,name='recipe_desc')
]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)