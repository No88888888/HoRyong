from rest_framework import serializers
from .models import Movies, Reviews, WishList, WatchedMovie, Keyword


class MoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    class MyReviewSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movies
            fields = '__all__'

    class Meta:
        model = Reviews
        fields = '__all__'
        read_only_fields = ('movie', 'user')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['movie'] = self.MyReviewSerializer(instance.movie).data
        return response


class KeywordsSerializer(serializers.ModelSerializer):
    class MyKeywordSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movies
            fields = '__all__'

    class Meta:
        model = Keyword
        fields = '__all__'
        read_only_fields = ('movie',)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['movie'] = self.MyKeywordSerializer(instance.movie).data
        return response


class WishListSerializer(serializers.ModelSerializer):

    class MyWishListSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movies
            fields = '__all__'

    class Meta:
        model = WishList
        fields = '__all__'
        read_only_fields = ('movie', 'user')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['movie'] = self.MyWishListSerializer(instance.movie).data
        return response


class WatchedMovieSerializer(serializers.ModelSerializer):

    class MyWatchedMovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movies
            fields = '__all__'

    class Meta:
        model = WatchedMovie
        fields = '__all__'
        read_only_fields = ('movie', 'user')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['movie'] = self.MyWatchedMovieSerializer(instance.movie).data
        return response
