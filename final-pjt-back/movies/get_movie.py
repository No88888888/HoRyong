from .models import Movies
import requests
# Create your views here.
movie_ids = [128246, 420817, 19995, 299534, 299536, 198277, 77866, 284052, 13, 109445, 672, 674, 767, 675, 673, 671, 771, 10191, 49530, 27205, 1726, 135397, 313369, 82695, 508, 77, 158445, 730823, 496243, 571783, 20342, 110415, 634649, 49026, 581528, 316029, 603, 479718, 619803, 15121, 129, 597, 361743, 396535, 14160, 752, 1016196, 10681, 791373, 269149]
def get_movie(request):

    for i in movie_ids:
        URL = f'https://api.themoviedb.org/3/movie/{i}?api_key=983a534de25475e797c8b4ef5617774b&language=ko-kr'
        print('id:',i)
        response = requests.get(URL).json()

        movie = response
        if movie['release_date'] == "":
            movie['release_date'] = '2000-01-01'
        added_movie = Movies(
            movie_id = movie['id'],
            title = movie['title'],
            poster_path = movie['poster_path'],
            backdrop_path = movie['backdrop_path'],
            overview = movie['overview'],
            release_date = movie['release_date'],
            genres = movie['genres'],
            popularity = movie['popularity'],
            vote_average = movie['vote_average'],
            
        )
        added_movie.save()