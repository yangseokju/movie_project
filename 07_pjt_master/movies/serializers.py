from rest_framework import serializers
from .models import Actor, Movie, Review


# actors 보여주기
class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'

# actors detail 에 넣으려고 만든거
class MovieListSerializer_Actor(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)

# actors detail 보여주기
class ActorListSerializer(serializers.ModelSerializer):

    movies = MovieListSerializer_Actor(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = '__all__'

# movies 보여주기
class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title','overview',)

# movies detail 에 넣으려고 만든거
class ReviewListSerializer_Movie(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title','content',)


# movies detail 에 넣으려고 만든거
class ActorListSerializer_Movie(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name',)


# movies detail 보여주기
class MovieListSerializer(serializers.ModelSerializer):

    actors = ActorListSerializer_Movie(many=True, read_only=True)
    review_set = ReviewListSerializer_Movie(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'


# reviews 보여주기
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title','content',)


# # reviews detail 에 넣을거 만들기
# class MovieListSerializer_review(serializers.ModelSerializer):

#     class Meta:
#         model = Movie
#         fields = ('title',)


# reviews detail 보여주기
class ReviewListSerializer(serializers.ModelSerializer):

    movie = MovieListSerializer_Actor(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'