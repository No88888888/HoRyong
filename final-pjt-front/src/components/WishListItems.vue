<template>
  <div>
    <div class="container">
      <div>
        <img :src="posterImg" alt="" class="">
        <h5>{{ wishlists.movie.title }}</h5>
      </div>
      <!-- <p>내 평점: {{review.score}}</p>
      <h5>{{ review.sentence }}</h5>
      <button @click="toMyReview">수정</button> -->
      <button @click="deleteWishList">삭제</button>
    </div>

  </div>
  <!-- <div>
    
    <h3>WishListItems</h3>
    <h3>{{wishlists.id}}</h3>
  </div> -->
</template>

<script>
import axios from 'axios'

export default {
  name : "WishListItems",
  props : {
    wishlist : Object,
    user_id : Number,
  },
  data() {
    return {
      wishlists : this.wishlist,
    }
  },
  computed: {
    posterImg() {
      const imgurl = 'https://image.tmdb.org/t/p/w220_and_h330_face/' + this.wishlists.movie.poster_path 
      return imgurl
    }
  },
  methods: {
    deleteWishList() {
      const API_URL ='http://127.0.0.1:8000'

      axios({
        method: 'delete',
        url: `${API_URL}/movies/${this.wishlists.movie.id}/modify_wishlist/${this.user_id}/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          console.log(res)
          this.$emit('renew-my-wishlists')
        })
        .catch((err) => {
          console.log(err)
        })
    },

  }
}
</script>

<style>

</style>