<template>
  <div class="movie-lists">
    <div>
      <h3>Movie List</h3>
      <p>{{getWatchedMovie}}</p>
      <div class="wrap-vertical"> 
        <MovieListsItem
        class="movie-items"
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
        @to-movie-list="toMovieView"
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
      },
      getWatchedMovie() {
        console.log('스토어에 저장된 워치드',this.$store.state.watchedMovie)
        return this.$store.state.watchedMovie
      },
    },
    created() {
      this.getMovies()
      this.getMyReview()
    },
    methods: {
      getMovies() {
        this.$store.dispatch('getMovies')
      },
      toMovieView(submitData) {
        this.$emit('to-movie-view', submitData)
      },
      getMyReview(){
        this.$store.dispatch('getMyReviews')
      }

    }

}
</script>

<style scoped>
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