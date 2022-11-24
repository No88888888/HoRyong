<template>
<!-- <div> -->
  <div id="app" :style="{ backgroundImage: 'linear-gradient(to bottom, rgba(0, 0, 0, 0.6) 10%, rgba(0, 0, 0, 0.7) 25%, rgba(0, 0, 0, 0.8) 50%, rgba(0, 0, 0, 0.9) 75%, rgba(0, 0, 0, 1) 100%), url(' + backdroppath + ')', backgroundSize: 'cover' }">
    <div class="dummy-box">
    </div>
    <div class="dummy-box">
    </div>
    <h3 class="fs-2"><b>KEYMOO's RECOMMEND</b></h3>
    <div class="dummy-box">
    </div>
    <div>
      <h4>{{ username }}님의 리뷰 키워드는</h4>
      <h4>"  {{ firstMovie.keyword }}  "</h4>
      <h4>입니다.</h4>
      <h4>해당 키워드로 추천 드릴 영화는</h4>
      <h3>"  {{ firstMovie.movie.title }}  "</h3>
      <h4>입니다.</h4>
      <div class="container my-5">
        <div class="row">
          <div class="col-2"></div>
          <div class="col-4">
            <img :src="firstMovieImg" alt="" />
            <div  @click="wishListToggle">
              <div class="d-flex justify-content-center align-items-center">
                <br>
                <h4>wishList 넣기</h4>
                <div class="dummy-box">
                </div>
                <i class="bi bi-bookmark-star" v-if="!is_wish_movie"></i>
                <i class="bi bi-bookmark-star-fill" v-if="is_wish_movie"></i>
              </div>
            </div>
          </div>
      
          <div class="col-4">
            <div class="dummy-box">
            </div>
            <h5>{{ username }} 님의 다른 키워드</h5>
            <span>
              두번 째 키워드:
              <div @click="changeToSecond"><h4>[  {{ secondMovie.keyword }}  ]</h4></div>
            </span>
            <div>
              <span>
                세번 째 키워드:
                <div @click="changeToThird"><h4>[  {{ thirdMovie.keyword }}  ]</h4></div>
              </span>
            </div>
            <div class="dummy-box">
            </div>
            <button class="glow-on-hover" @click="myWishList">Go To WishList</button>
          </div>
        </div>
      </div>
      <!-- 컨테 -->
    <div class="dummy-box">
    </div>
    <div class="dummy-box">
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
      const wishlists = this.$store.state.wishlist.data
      if (wishlists) {
        console.log(wishlists)
        for (let wish of wishlists) {
          if (wish.movie.id === this.firstMovie.movie.id && wish.user === this.user_id) {
            return true
          } 
        }
        return false
      }
      return false
    },
    backdroppath() {
      return (
        'https://image.tmdb.org/t/p/original' +
        this.$store.state.recommendMovie[0].movie.backdrop_path
      );
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
      
    },
    myWishList() {
      this.$router.push({ name: "WishList" });
    }
  }
};
</script>

<style>
i {
font-size: 37px;
}
.dummy-box{
  height:50px;
  width:20px;
}
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