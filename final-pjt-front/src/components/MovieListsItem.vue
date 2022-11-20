<template>
  <div>
    <img :src="posterImg" alt="">
    <h5>{{ movie.title }}</h5>
    <router-link :to="{ name: 'DetailView', params: { id: movie.id } }">
      <button>GET DETAIL</button>
    </router-link>
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

</style>