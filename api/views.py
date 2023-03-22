from django.shortcuts import render
from rest_framework import generics
from .serializers import MovieSerializer
from .models import Movie

# Create your views here.
class MovieView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
