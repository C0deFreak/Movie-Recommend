from django.db import models

# All the details about a single movie
class Movie(models.Model):

    # Unique movie name to distinguish from other movie
    name = models.CharField(max_length=70, unique=True, default='')

    # Genre of the movie for subcategorization. Possible genres: Action, Comedy, Drama, Fantasy, Horror, Mystery, Romance, Thriller, Western, SCI-FI
    genre = models.CharField(max_length=7, unique=False, default='')

    # Appropriate age for this movie
    age = models.IntegerField(null=False, default=False)

    # A short description of the movie
    description = models.CharField(max_length=500, unique=True, default='')

    # The overall rating of the movie
    rating = models.IntegerField(null=False, default=False)

