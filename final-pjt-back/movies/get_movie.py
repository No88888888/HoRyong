from .models import Movies
import requests
import json
# Create your views here.
movie_id = [128246, 420817, 19995, 299534, 299536, 198277, 77866, 284052, 13, 19445, 672, 674, 767, 675, 673, 671, 771, 1191, 49530, 27205, 1726, 135397, 313369, 82695, 508, 77, 158445, 730823, 496243, 571783, 20342, 110415, 634649, 49026, 581528, 316029, 603, 479718, 619803, 15121, 129, 597, 361743, 396535, 14160, 752, 116196, 1681, 791373, 269149]
def get_movie():

    for i in movie_id:
        URL = f'https://api.themoviedb.org/3/movie/{i}?api_key=983a534de25475e797c8b4ef5617774b&language=ko-kr'

        response = requests.get(URL).json()
        movies = response

        for movie in movies:
            added_movie = Movies(       
                movie_id = movie['id'],   
                title = movie['title'],
                poster_path = movie['poster_path'],
                backdrop_path = movie['backdrop_path'],
                overview = movie['overview'],
                release_date = movie['release_date'],
                genres = json.dumps(movie['genres']),  # 리스트를 str으로 만들어주는 과정
                popularity = movie['popularity'],
                vote_average = movie['vote_average'],
                # genre_names = json.dumps()
            )
            added_movie.save()


    # return render(request, 'movies/') # 이건 그냥 return 하려고 했던거라 굳이 신경 안 써도 됨
get_movie()