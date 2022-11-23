<template>
  <div>
    <h1>Wish List</h1>
    <WishListItems
    class="wishlist-items"
    v-for="wishlist in wishlists"
    :key="wishlist.id"
    :wishlist="wishlist"
    />
    <h3>{{wishMovie}}</h3>
  </div>
</template>

<script>
import WishListItems from '@/components/WishListItems'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "WishList",
  components: {
    WishListItems,
  },
  data() {
    return {
      wishlists : [],
      user_id : null,
      username: null,
    }
  },
  
  computed: {
    wishMovie() {
      return this.wishlists
    }
  },
  created() {
    this.getUserPk(),
    this.wishListMovie()
  },
  methods: {
    getUserPk() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
            this.user_id = res.data.pk
            console.log(this.user_id)
            this.username = res.data.username
            return {'user_id': res.data.pk}
      })
        .then((res) => {
          const user_id = res.user_id
          axios({
            methods: 'get',
            url: `${API_URL}/movies/wish_list/${user_id}/`,
            data: {
              user_pk: user_id,
            },
            header: {
              Authorization: `Token ${ this.$store.state.token }`
            }
          })
          .then((res) => {
            this.wishlists = res.data
          })
      })
    },
    wishListMovie() {
      const mywishlist = this.$store.state.wishlist.data
      for (let wish of mywishlist) {
        // console.log(wish.user)
        if (wish.user === this.user_id) {
          this.wishlists.push(wish)
        } 
      }
      // console.log(this.wishlists)
      return this.wishlists
    }
  }
  
}
</script>

<style>

</style>