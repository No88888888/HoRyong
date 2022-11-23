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
          <div>
            <h2>{{ movie.title }}</h2>
          </div>
          <div class="movie-overview">
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
    }
  },
  computed: {
    renderwatchUrl() {
      return this.watchUrl
    }
  },
  created() {
    this.getMovieDetail()
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
.movie-overview p{
  display: "flex";
  justify-content: "start";
}
</style>