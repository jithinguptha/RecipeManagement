from django.contrib.auth.models import User
from django.db import models



# Create your models here.

class Recipes(models.Model):
    cuisine_choice = (
        ("Chinese", "Chinese"),
        ("Indian", "Indian"),
        ("Japanese", "Japanese")
    )

    meal_choice = (
        ("Breakfast", "Breakfast"),
        ("Lunch", "Lunch"),
        ("Dinner", "Dinner")
    )
    name = models.CharField(max_length=20)
    cuisine = models.CharField(max_length=40, choices=cuisine_choice, default='indian')
    meal_type = models.CharField(max_length=20, choices=meal_choice)
    ingrediant = models.CharField(max_length=20, default='')
    desc = models.TextField(default='')
    image = models.ImageField(upload_to='recipe/image', null=True, blank=True)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    recipes=models.ForeignKey(Recipes,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    review=models.TextField(default='')
    rating=models.IntegerField(choices=((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')),default='5')
    date=models.DateTimeField(auto_now_add=True)
