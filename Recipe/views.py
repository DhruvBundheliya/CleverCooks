from django.shortcuts import render,redirect
from .models import Recipe
from django.views import View

def index(request):
    return render(request,'index.html')

def postrecipe(request):
    if request.method == 'POST':s
        title = request.POST['title']
        image = request.POST['image']
        serves = request.POST['serves']
        time = request.POST['time']
        ingredients = request.POST['ingredients']
        steps = request.POST['steps']
        recipe = Recipe(title=title, image=image,serves=serves,time=time,ingredients=ingredients,steps=steps)
        recipe.save()
    return render(request,'post_recipe.html')


def recipes(request):
    recipedetails = Recipe.objects.all()
    return render(request,'recipes.html')

def recipe_desc(request):
    return render(request,'recipe_desc.html')