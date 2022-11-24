<template>
  <div>
    <div class="dummy-box">
    </div>
    <div class="container my-5">
      <div class="row">
        <div class="col-4">
        <img :src="posterImg" alt="">
        <br>
        <br>
        <h5>{{title}}</h5>
        </div>
        <div class="col-8"> 
          <h5>평점 : {{vote_average}}</h5>
          <h5>장르 : {{genres}} </h5>
          <div class="dummy-box">
          </div>
          <h5>{{overview}}</h5>
        </div>
      </div>
    </div>
    <hr>
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
    title() {
      const wishtitle = this.toWishDetail.movie.title
      return wishtitle
    },
    overview() {
      const wishoverview = this.toWishDetail.movie.overview
      return wishoverview
    },
    vote_average() {
      const wishvoteaverage =  this.toWishDetail.movie.vote_average
      return wishvoteaverage
    }
  },
}
</script>

<style>
.dummy-box{
  height:50px
}
</style>