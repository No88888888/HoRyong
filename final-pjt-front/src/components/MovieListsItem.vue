<template>
  <div>
    <div class="img-content">
      <img :src="posterImg" alt="">
      <div class="zoom">
        <router-link :to="{ name: 'DetailView', params: { id: movie.id } }">
          <button>GET DETAIL</button>
        </router-link>
        <button>리뷰 작성</button>
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
    computed: {
      posterImg() {
        const imgurl = 'https://image.tmdb.org/t/p/w220_and_h330_face/' + this.movie.poster_path 
        return imgurl
      }
    }
}
</script>

<style>
.zoom {
  display: none;
}
.img-content:hover .zoom{
  display: block;
}
</style>