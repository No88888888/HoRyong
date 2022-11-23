<template>
  <div >
    <div>
    <div class="container">
      <img :src="posterImg" alt="" class="image" v-bind:class="{'selected': isSelected}">
      <div class="zoom">
        <div>
          <router-link :to="{ name: 'DetailView', params: { id: movie.id } }">
            <button>GET DETAIL</button>
          </router-link>
        </div>
        <div>
          <button v-if="isSelected" @click="toMovieList">리뷰 작성</button>
        </div>
      </div>
    </div>
    <h5>{{ movie.title }}</h5>
  </div>
  <button v-if="isLogedIn" @click="watchedMovie">Watched</button>
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
      isSelected: false
    }
  },
  computed: {
    posterImg() {
      const imgurl = 'https://image.tmdb.org/t/p/w220_and_h330_face/' + this.movie.poster_path 
      return imgurl
    },
    isLogedIn() {
      return this.$store.state.username
    },
    watchedMovieList() {
      return this.$store.state.watchedMovie
    }
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
        console.log("리스폰스", res.data)
        this.$store.dispatch('saveWatchedMovie', res.data)
        return res
      })
      .then((res) => {
        console.log("리스폰스2", res.data)
        this.watchedOrNot()
      })
    },
    // 여기서 부터 태그 관련 함수
    watchedOrNot() {
      if (this.watchedMovieList?.includes(this.movie.id)) {
        this.isSelected = true
      } else {
        this.isSelected = false
      }
      console.log(this.isSelected)
    }
  },
  created() {
    this.watchedOrNot()
  }
}

</script>

<style>
.selected {
  padding:4px;
  border: 4px solid red;
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

