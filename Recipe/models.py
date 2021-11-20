from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
    

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    image= models.ImageField(upload_to="RecipeImage")
    serves = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    ingredients = models.TextField()
    steps = models.TextField()

    def __str__(self):
        return self.title
