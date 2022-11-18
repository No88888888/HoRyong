<template>
  <div>
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
    }
}
</script>

<style>

</style>