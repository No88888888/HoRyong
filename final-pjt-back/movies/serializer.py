from rest_framework import serializers
from .models import Movies, Reviews, WishList, WatchedMovie, Keyword


# class MoviesListSerializer(serializers.ModelSerializer):
#     # username = serializers.CharField(source='user.username', read_only=True)

#     class Meta:
#         model = Movies
#         # fields = ('id', 'title', 'content')
#         fields = ('title', 'poster_path')

# class MoviesSerializer(serializers.ModelSerializer):
#     comment_set = ReviewsSerializer(many=True, read_only=True)
#     comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
#     username = serializers.CharField(source='user.username', read_only=True)

#     class Meta:
#         model = Movies
#         fields = '__all__'
        # read_only_fields = ('user' )


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
            fields = ('movie_id', 'poster_path', 'title', 'overview', 'vote_average',)
        
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