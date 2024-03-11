from recipes.models import Recipes

from rest_framework import serializers
from rest_framework.authtoken.admin import User

from recipes.models import Reviews


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ['id', 'name', 'cuisine', 'meal_type', 'ingrediant', 'image', 'desc']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['username', 'password']

    def create(self, validate_data):
        u = User.objects.create_user(username=validate_data['username'], password=validate_data['password'])
        u.save()
        return u


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id', 'recipes', 'user', 'review', 'rating', 'date']
