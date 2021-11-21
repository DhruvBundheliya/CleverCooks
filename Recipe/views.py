from django.shortcuts import render,redirect
from .models import Recipe
from django.views import View

def index(request):
    return render(request,'index.html')

def postrecipe(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        coverImage = request.POST['coverImage']
        serves = request.POST['serves']
        time = request.POST['time']
        ingredients = request.POST['ingredients']
        instructions = request.POST['instructions']
        recipe = Recipe(title=title,description=description, coverImage=coverImage,serves=serves,time=time,ingredients=ingredients,instructions=instructions)
        recipe.save()
        return render(request,'recipes.html')
    return render(request,'post_recipe.html')


def recipes(request):
    recipedetails = Recipe.objects.all()
    context = {'recipedetails' : recipedetails}
    return render(request,'recipes.html', context)

def recipe_desc(request):
    return render(request,'recipe_desc.html')