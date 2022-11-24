<template>
  <div>
    <div class="container">
      <div @click="toDetail">
        <img :src="posterImg" alt="" class="" >
        <h5>{{ wishlists.movie.title }}</h5>
      </div>
      <button class="glow-on-hover" @click="deleteWishList">삭제</button>
    </div>
    <div class="dummy-box">
    </div>
  </div>
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
    toDetail() {
      console.log('가자', this.wishlists)
      this.$emit('wishmovie-detail', this.wishlists)
    }
  }
}
</script>

<style>
.glow-on-hover {
    width: 150px;
    height: 50px;
    border: none;
    outline: none;
    color: #fff;
    background: #111;
    cursor: pointer;
    position: relative;
    z-index: 0;
    border-radius: 10px;
}

.glow-on-hover:before {
    content: '';
    background: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
    position: absolute;
    top: -2px;
    left:-2px;
    background-size: 400%;
    z-index: -1;
    filter: blur(5px);
    width: calc(100% + 4px);
    height: calc(100% + 4px);
    animation: glowing 20s linear infinite;
    opacity: 0;
    transition: opacity .3s ease-in-out;
    border-radius: 10px;
}

.glow-on-hover:active {
    color: #000
}

.glow-on-hover:active:after {
    background: transparent;
}

.glow-on-hover:hover:before {
    opacity: 1;
}

.glow-on-hover:after {
    z-index: -1;
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    background: #111;
    left: 0;
    top: 0;
    border-radius: 10px;
}
@keyframes glowing {
    0% { background-position: 0 0; }
    50% { background-position: 400% 0; }
    100% { background-position: 0 0; }
}
</style>