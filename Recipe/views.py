from django.shortcuts import render,redirect, HttpResponse
from .models import Recipe, Newsletter
from django.views import View

def index(request):
    recipes = Recipe.objects.all()
    if request.method == 'POST':
         emailaddress = request.POST['emailaddress']
         newsletter= Newsletter(emailaddress=emailaddress)
         newsletter.save()
    return render(request,'index.html',{'recipes':recipes})

def aboutus(request):
    return render(request,'aboutus.html')

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
        return redirect('recipes')
    return render(request,'post_recipe.html')


def recipes(request):
    recipes = Recipe.objects.all()
    return render(request,'recipes.html',{'recipes':recipes})

def recipe_desc(request, id):
    recipedetails = Recipe.objects.filter(id = id)[0]
    recipes = Recipe.objects.all()
    context = {'recipedetails' : recipedetails , 'recipes':recipes}
    return render(request,'recipe_desc.html', context)

def search(request):
    query = request.GET['query']
    recipes = Recipe.objects.filter(title__icontains=query)
    params = {'recipes' : recipes}
    return render(request,'search.html',params)