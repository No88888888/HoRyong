<template>
  <div>
    <h1>Detail</h1>
    <p>영화 제목: {{ movie?.id }}</p>
    <p>줄거리: {{ movie?.overviews }}</p>
    <p>장르: {{ movie?.genres }}</p>

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
    }
  },
  created() {
    this.getMovieDetail()
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}`
      })
        .then((res) => {
          console.log(res)
          this.movie = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style>

</style>