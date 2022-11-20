<template>
  <div>
    <h1>Detail</h1>
    <div class="single_column">
      <section id="original_header" class="images inner">
        <!-- 여기가 포스터 -->
        <div>
          <div class="poster">
            <img src="movie.poster_path" alt="movie.title">
          </div>
          <div class="ott_offer">
            <div class="button">
              <div class="text">
                <span>
                  <h4>Now Streaming</h4>
                  <a class="no_click" href="watchUrl" title="#">Watch Now</a>
                </span>
              </div>
            </div>
          </div>
        </div>
        <!-- 여기가 제목 평점 및 내용 -->
        <div></div>
      </section>
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
    }
  },
  created() {
    this.getMovieDetail()
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.id}/detail`
      })
        .then((res) => {
          console.log(1,res)
          this.movie = res.data
          console.log(this.movie)
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
        url: `https://api.themoviedb.org/3/movie/${this.movie.id}/watch/providers?api_key=${this.tmdbAPIKey}`
      })
        .then((res) => {
          console.log(res)
        })
    }
  }
}
</script>

<style>

</style>