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
        <p> WishList </p>
        <button style="border:none; background-color:white;" @click="doSend">
          추가 
        </button>
        
      <h2>{{ username }} 님의 다른 키워드</h2>
    </div>
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

<script src="https://kit.fontawesome.com/69c09758b6.js" crossorigin="anonymous"></script>
<script>
import WishListItems from '@/components/WishListItems'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "RecommendView",
  data() {
    return {
      movie: this.$store.state.recommendMovie,
      user_id : null,
    };
  },
  
  computed: {
    firstMovie() {
      return this.$store.state.recommendMovie[0];
    },
    username() {
      console.log(this.$store.state.username);
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
    doSend() {
      const payload = {
        pk: this.user_id,
        movie_id: this.movie.id,
        user_id:this.user_id, 
      }
      this.$store.dispatch('submitWishList', payload)
    },
    wishList() {
      const API_URL =`${API_URL}/movies/wish_list/${this.user_id}/`
      axios({
        method: 'post',
        url: API_URL,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.$store.dispatch('saveWishList', res.data)
      })
    },
  }
};
</script>

<style>
</style>