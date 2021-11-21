from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
    

class Recipe(models.Model):
    #recipe_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    coverImage= models.ImageField(upload_to="RecipeImage")
    serves = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    ingredients = models.TextField()
    instructions = models.TextField()
    #pub_date = models.DateField()

    def __str__(self):
        return self.title
