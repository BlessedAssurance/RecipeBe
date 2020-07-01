import json

from django.conf import settings
from django.contrib.auth.models import User
from django.core import serializers
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import Country,  Recipe, Profile, RecipeIngredient
from .serializer import (CountrySerializer, 
                         RecipeSerializer, ProfileSerializer,
                         RecipeIngredientSerializer, UserSerializer)
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset= User.objects.all()
    serializer_class = UserSerializer
      

class UserDetails(generics.RetrieveDestroyAPIView):
    queryset= User.objects.all()
    serializer_class = UserSerializer
    lookup_field='username'


class ProfileList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
        

class Profiledetails(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated)  
    serializers = ProfileSerializer
    queryset = Profile.objects.all()


class IngredientList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class Ingredientdetails(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated)  
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field='name'

class CountryList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated)
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
       

class Countrydetails(generics.RetrieveDestroyAPIView): 
    #  # permission_classes = (IsAuthenticated)
    queryset = Country.objects.all()
    lookup_field='place'
    serializer_class = CountrySerializer
    
class RecipeIngredientList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated)
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer
     

class RecipeIngredientdetails(generics.RetrieveUpdateDestroyAPIView):  
    # permission_classes = (IsAuthenticated)
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer
    lookup_field = 'name'


class Recipes(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    filter_backends=[filters.SearchFilter]
    search_fields = ['country','name','ingredients']

    def perform_create(self, serializer):
        serializer.save(user=Profile.objects.first())

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

class RecipesCountry(generics.ListAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

    def get_queryset(self):
        country = self.kwargs['country']
        return Recipe.objects.filter(country=country)


class RecipesIngredients(generics.ListAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

    def get_queryset(self):
        ingredients = self.kwargs['ingredients']
        return Recipe.objects.filter(ingredients__icontains=ingredients)
        













