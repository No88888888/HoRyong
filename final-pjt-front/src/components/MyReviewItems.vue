<template>
  <div>
    <div class="container">
      <div>
        <img :src="posterImg" alt="" class="">
        <h5>{{ review.movie.title }}</h5>
      </div>
      <h3>{{ review.sentence }}</h3>
    </div>

  </div>
</template>

<script>
export default {
  name: "MyReviewItems",
  props:{
    review: Object
  },
  computed: {
    posterImg() {
      const imgurl = 'https://image.tmdb.org/t/p/w220_and_h330_face/' + this.review.movie.poster_path 
      return imgurl
    }
  },
}
</script>

<style>

</style>