<template>
  <div>
    <div
    @click="watchedMovie"
    >
    <div class="container">
      <img :src="posterImg" alt="" class="image">
      <div class="zoom">
        <div>
          <router-link :to="{ name: 'DetailView', params: { id: movie.id } }">
            <button>GET DETAIL</button>
          </router-link>
        </div>
        <div>
          <button @click="toMovieList">리뷰 작성</button>
        </div>
      </div>
    </div>
    <h5>{{ movie.title }}</h5>
  </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name : 'MovieListsItem',
  props: {
      movie: Object,
  },
  data() {
    return {
      submitData : {
        movie: this.movie,
        modal: true,
      },
      isActive: false
    }
  },
  computed: {
    posterImg() {
      const imgurl = 'https://image.tmdb.org/t/p/w220_and_h330_face/' + this.movie.poster_path 
      return imgurl
    },
  },
  methods: {
    toMovieList() {
      this.$emit('to-movie-list', this.submitData)
    },
    watchedMovie() {
      const API_URL =`http://127.0.0.1:8000/movies/${this.movie.id}/watched_movie/`
      axios({
        method: 'post',
        url: API_URL,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) =>{
        console.log("와치드 무비", res.data)
        this.$store.dispatch('saveWatchedMovie', res.data)
      })
    }
  }
}

</script>

<style>
.isActive {
  padding:4px;
  background-color: orange;
}
.container {
  position: relative;
  width: 50%;
}

.image {
  opacity: 1;
  display: block;
  transition: .5s ease;
  backface-visibility: hidden;
}

.zoom {
  transition: .5s ease;
  opacity: 0;
  position: absolute;
  top: 50%;
  left: 100%;
  transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  text-align: center;
}

.container:hover .image {
  opacity: 0.3;
  filter: blur(4px);
}

.container:hover .zoom {
  opacity: 1;
}
</style>

