# Generated by Django 3.2.6 on 2021-11-21 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('recipe_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('coverImage', models.ImageField(upload_to='RecipeImage')),
                ('serves', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
            ],
        ),
    ]
