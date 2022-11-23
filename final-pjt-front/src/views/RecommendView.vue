<template>
  <div>
    <h1>Recommend Page</h1>
    <div>
      <h2>{{ username }} 님이 작성하신 리뷰의 키워드는</h2>
      <h2>"{{ firstMovie.keyword }}"입니다.</h2>
      <h2>해당 키워드로 추천 드릴 영화는</h2>
      <h3>"{{ firstMovie.movie.title }}" 입니다.</h3>
      <img :src="firstMovieImg" alt="" />
    <div>
        <div @click="wishListToggle">
          <i class="bi bi-bookmark-star" v-if="!is_wish_movie"></i>
          <i class="bi bi-bookmark-star-fill" v-if="is_wish_movie"></i>
        </div>
    </div>
      <h2>{{ username }} 님의 다른 키워드</h2>
      <div>
        <span>
          두번 째 키워드:
          <div @click="changeToSecond">{{ secondMovie.keyword }}</div>
        </span>
      </div>
      <div>
        <span>
          세번 째 키워드:
          <div @click="changeToThird">{{ thirdMovie.keyword }}</div>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "RecommendView",
  data() {
    return {
      movie: this.$store.state.recommendMovie,
      user_id : null,
      is_wishlist : null,
    };
  },
  
  computed: {
    is_wish_movie() {
      const wishlists = this.$store.state.wishlist
      console.log(this.user_id)
      for (let wish of wishlists) {
        if (wish.data.movie.id === this.firstMovie.movie.id && wish.user === this.user_id) {
          return true
        } 
      }
      return false
    },
    firstMovie() {
      return this.$store.state.recommendMovie[0];
    },
    username() {
      return this.$store.state.username;
    },
    firstMovieImg() {
      return (
        "https://image.tmdb.org/t/p/w220_and_h330_face/" +
        this.$store.state.recommendMovie[0].movie.poster_path
      );
    },
    secondMovie() {
      return this.$store.state.recommendMovie[1];
    },
    thirdMovie() {
      return this.$store.state.recommendMovie[2];
    },
  },
  created() {
    this.getUserPk()
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
            return {'user_id': res.data.pk}
      })
    },
    changeToSecond() {
      this.$store.dispatch("switchWithSecond");
      this.$router.push({ name: "RecommendView" });
      this.$router.go();
    },
    changeToThird() {
      this.$store.dispatch("switchWithThird");
      this.$router.push({ name: "RecommendView" });
      this.$router.go();
    },
    wishListToggle() {
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.firstMovie.movie.id}/modify_wishlist/${this.user_id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          this.$store.dispatch('saveWishList', res)
        })
      
    }
  }
};
</script>

<style>
</style>