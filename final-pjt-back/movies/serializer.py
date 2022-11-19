from rest_framework import serializers
from .models import Movies, Reviews


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




class ReviewsSerializer(serializers.ModelSerializer):
    class MyReviewSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movies
            fields = ('movie_id', 'poster_path', 'title','overview',)
        
    class Meta:
        model = Reviews
        fields = '__all__'
        read_only_fields = ('movie', 'user')
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['movie'] = self.MyReviewSerializer(instance.movie).data
        return response