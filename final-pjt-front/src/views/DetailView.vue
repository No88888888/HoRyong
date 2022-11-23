<template>
  <div id="app" :style="{ backgroundImage: 'linear-gradient(to bottom, rgba(0, 0, 0, 0.6) 10%, rgba(0, 0, 0, 0.7) 25%, rgba(0, 0, 0, 0.8) 50%, rgba(0, 0, 0, 0.9) 75%, rgba(0, 0, 0, 1) 100%), url(' + backdroppath + ')', backgroundSize: 'cover' }">
    <h1 class="mb-5">Detail</h1>
    <div class="dummy-box">
    </div>
    <div class="container my-5">
      <div class="row">
        <div class=" single_column col-4">
          <!-- <section id="original_header" class="main"> -->
            <!-- 여기가 포스터 -->
          <div class="poster">
            <img :src="imgUrl" alt="#" class="image-sized">
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
    <div>
      <DetailReviews
      class="review-items"
      v-for="(review,index) in reviews"
      :key="review.id"
      :review="review"
      :index="index"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import DetailReviews from '@/components/DetailReviews'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  components:{
    DetailReviews,
  },
  data() {
    return {
      movie: null,
      watchUrl: null,
      tmdbAPIKey: 'eb54cff7c77bbeb1441eaa6be7f211a1',
      imgUrl: '',
      reviews: null,
      backdrop : null,
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
    backdroppath() {
      return this.backdrop
      
    }
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
          this.backdrop = 'https://image.tmdb.org/t/p/original' + this.movie.backdrop_path
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
        this.reviews = res.data
        console.log('this.reviews', this.reviews)
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
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');
#app {
  font-family: 'Noto Sans KR', sans-serif, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: white;
  height: 100%;
  /* background: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0.6) 10%,
    rgba(0, 0, 0, 0.7) 25%,
    rgba(0, 0, 0, 0.8) 50%,
    rgba(0, 0, 0, 0.9) 75%,
    rgba(0, 0, 0, 1) 100%
  ), url(https://image.tmdb.org/t/p/original/7RyHsO4yDXtBv1zUU3mTpHeQ0d5.jpg);
  background-size: cover; */
}
.dummy-box{
  height:50px
}
.poster > img {
  max-width: 100%;
  height: auto;
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
.review-items {
  text-align: left;
}


</style>