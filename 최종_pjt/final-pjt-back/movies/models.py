from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    users_pick = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='movies_picked')
    movie_id = models.CharField(max_length=100)
    title  = models.CharField(max_length=100)
    overview = models.TextField()
    genre = models.ManyToManyField(Genre, related_name='movies')
    poster_path = models.CharField(max_length=500)
    backdrop_path = models.CharField(max_length=500)
    popularity = models.IntegerField()
    release_date = models.CharField(max_length=100)
    vote_avg = models.FloatField()
    vote_cnt = models.IntegerField()


# class Article(models.Model):
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='articles')
#     movie_title = models.CharField(max_length=500)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
#     username = models.CharField(max_length=100)
#     ########
#     rating = models.FloatField()
#     ########
#     title = models.CharField(max_length=500)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    

# class Comment(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
#     username = models.CharField(max_length=100)
#     article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
#     content = models.CharField(max_length=500)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')