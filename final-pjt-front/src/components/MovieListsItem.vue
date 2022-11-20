<template>
  <div>
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
</template>

<script>
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
        }
      }
    },
    computed: {
      posterImg() {
        const imgurl = 'https://image.tmdb.org/t/p/w220_and_h330_face/' + this.movie.poster_path 
        return imgurl
      }
    },
    methods: {
      toMovieList() {
        this.$emit('to-movie-list', this.submitData)
      }
    }
}
</script>

<style>
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

