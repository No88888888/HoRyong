<template>
  <div>
    <h1 class="mb-5">Detail</h1>
    <div class="dummy-box">
    </div>
    <div class="container my-5">
      <div class="row">
        <div class=" single_column col-4">
          <!-- <section id="original_header" class="main"> -->
            <!-- 여기가 포스터 -->
          <div class="poster">
            <img :src="imgUrl" alt="#">
          </div>
          <!-- 나우 워치로 보낼 디브 -->
          <div class="ott_offer">
            <div class="button">
              <div class="text">
                <span>
                  <h4>Now Streaming</h4>
                  <a class="no_click" :href="renderwatchUrl" title="#" target="_blank">Watch Now</a>
                </span>
              </div>
            </div>
          </div>
        </div>
          <!-- 여기가 제목 평점 및 내용 -->
        <div class="movie-info col-8">
          <div class="movie-title">
            <h2>{{ movie.title }}  ({{year}})</h2>
          </div>
          
          <div class="dummy-box">
          </div>
          <div class="movie-rate">
            <p>평점: {{ movie.vote_average }}</p>
            <p>장르: {{ genres }}</p>
          </div>
          
          <div class="movie-overview">
            <h5>개요</h5>
            <p>{{ movie.overview }}</p>
          </div>
        </div>
      </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  data() {
    return {
      movie: null,
      watchUrl: null,
      tmdbAPIKey: 'eb54cff7c77bbeb1441eaa6be7f211a1',
      imgUrl: '',
      reviews: null,
    }
  },
  computed: {
    renderwatchUrl() {
      return this.watchUrl
    },
    year() {
      const cut = this.movie.release_date.substr(0, 4);
      return cut
    },
    genres() {
      const genreitems = this.movie.genres
      console.log(genreitems)
      let genrename = ''
      genreitems.forEach((genre) => {
        genrename += genre.name + ', '
      })
      let result = genrename.slice(0, -2);
      return result
    },
  },
  created() {
    this.getMovieDetail()
    this.getMovieReviews()
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.id}/`
      })
        .then((res) => {
          this.movie = res.data
          this.imgUrl = 'https://image.tmdb.org/t/p/w220_and_h330_face/' + this.movie.poster_path
          return res.data
        })
        .then((res) => {
          console.log(2,res)
          this.getWatchUrl()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getMovieReviews(){
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.id}/movie_review/`
      })
      .then((res) => {
        console.log('res.data', res.data)
        this.reviews = res.data
      })
    },
    getWatchUrl() {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.movie.movie_id}/watch/providers?api_key=${this.tmdbAPIKey}`
      })
        .then((res) => {
          console.log(res.data.results.KR.link)
          this.watchUrl = res.data.results.KR.link
          return this.watchUrl
        })
    }
  }
}
</script>

<style scoped>
.dummy-box{
  height:50px
}
.movie-title h2{
  position:relative;
  text-align:left;
}
.movie-rate p{
  position:relative;
  text-align:left;
}
.movie-overview p{
  position:relative;
  text-align:left;
}
.movie-overview h5{
  position:relative;
  text-align:left;
  font-weight: bold;
}


</style>