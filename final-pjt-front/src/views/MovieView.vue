<template>
  <div>
    <h1>Movie Page</h1>
    <hr>
    <MovieLists/>
  </div>
</template>

<script>
import MovieLists from '@/components/MovieLists'

export default {
    name : 'MovieView',
    components: {
        MovieLists
    }
}
</script>

<style>

</style>