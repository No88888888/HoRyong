<template>
  <div class="movie-lists">
    <h3>Movie List</h3>
    <MovieListsItem
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script>
import MovieListsItem from '@/components/MovieListsItem'

export default {
    name: "MovieLists",
    components: { 
        MovieListsItem,
    },
    computed:{
      movies() {
        return this.$store.state.movies
      }
    },
    created() {
      this.getMovies()
    },
    methods: {
      getMovies() {
        this.$store.dispatch('getMovies')
      }
    }

}
</script>

<style>
.movie-list {
  text-align: start;
}
</style>