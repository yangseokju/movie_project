from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Movie
from .serializers import (
    MovieListSerializer, 
    MovieDetailSerializer,
    GenreListSerializer,
)

User = get_user_model()

# Create your views here.
@api_view(['GET'])
def get_movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def wish_movies_add(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.wish_users.filter(pk=request.user.pk).exists():
        movie.wish_users.remove(request.user)
    else:
        movie.wish_users.add(request.user)
    return Response(status=status.HTTP_200_OK)




# @api_view(['GET', 'POST'])
# def article_list_or_create(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)

#     if request.method == 'GET':
#         articles = Article.objects.filter(movie=movie)
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         # 해당 영화에 대해 현재 유저가 작성한 리뷰가 이미 존재할 경우
#         if Article.objects.filter(user=request.user).filter(movie=movie).exists():
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(movie=movie, user=request.user, username=request.user.username, movie_title=movie.title)
#             return Response(serializer.data)


# # @permission_classes([IsAuthenticated])
# @api_view(['GET','PUT','DELETE'])
# def article_update_or_delete(request, movie_pk, article_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     article = get_object_or_404(Article, pk=article_pk)
    
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     if article.user != request.user:
#         return Response(status=status.HTTP_401_UNAUTHORIZED)

#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
    
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['POST'])
# def comment_create(request, movie_pk, article_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     article = get_object_or_404(Article, pk=article_pk)
#     serializer = CommentSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(movie=movie, article=article, user=request.user, username=request.user.username)
#         return Response(serializer.data)

# @api_view(['PUT', 'DELETE'])
# def comment_update_or_delete(request, movie_pk, article_pk, comment_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     article = get_object_or_404(Article, pk=article_pk)
#     comment = get_object_or_404(Comment, pk=comment_pk)
#     if request.method == 'PUT':
#         serializer = CommentSerializer(instance=comment, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(movie=movie, article=article)
#             return Response(serializer.data)
#     elif request.method == 'DELETE':
#         comment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['POST'])
# def article_like(request, movie_pk, article_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     article = get_object_or_404(Article, pk=article_pk)
    
#     if article.like_users.filter(pk=request.user.pk).exists():
#         article.like_users.remove(request.user)
#     else:
#         article.like_users.add(request.user)
#     return Response(status=status.HTTP_200_OK)

