<template>
  <div class="movie-lists">
    <div>
      <h3>Movie List</h3>
      <div class="wrap-vertical"> 
        <MovieListsItem
        class="movie-items"
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
        />
      </div>
    </div>
  </div>
</template>

<script>
import MovieListsItem from '@/components/MovieListsItem'

export default {
    name: "MovieLists",
    data() {
      return {
      }
    },
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
      },
    }

}
</script>

<style>
.movie-list {
  text-align: start;
}
.wrap-vertical{
   /* 가로 스크롤 */
  overflow: auto;
  white-space: nowrap;
}
.movie-items {
  display: inline-block;
  color: rgb(0, 0, 0);
  text-align: center;
  text-decoration: none;
  padding: 14px;
}
</style>