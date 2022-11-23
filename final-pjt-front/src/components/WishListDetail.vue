<template>
  <div>
    <img :src="posterImg" alt="">
    <h3>{{this.toWishDetail.movie.title}}</h3>
    <h4>{{this.toWishDetail.movie.overview}}</h4>
    <h4>평점 : {{this.toWishDetail.movie.vote_average}}</h4>
    <h4>장르 : {{genres}}</h4> 
  </div>
  
</template>

<script>
export default {
  name: 'WishListDetail',
  props: {
    toWishDetail: Object,
  },
  computed: {
    posterImg() {
      const imgurl = 'https://image.tmdb.org/t/p/w220_and_h330_face/' + this.toWishDetail.movie.poster_path 
      return imgurl
    },
    genres() {
      const genreitems = this.toWishDetail.movie.genres
      console.log(genreitems)
      let genrename = ''
      genreitems.forEach((genre) => {
        genrename += genre.name + ', '
      })
      let result = genrename.slice(0, -2);
      return result
    },
    // title() {
    //   const
    // }
  },
}
</script>

<style>

</style>