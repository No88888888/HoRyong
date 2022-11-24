<template>
  <div>
    <div class="dummy-box">
    </div>
    <div class="container my-5">
      <div class="row">
        <div class="col-4">
          <div class="poster">
            <img :src="posterImg" alt="" class="image-sized">
          </div>
          <br>
            <h5 class="movie-title">{{ review.movie.title }}</h5>
        </div>
      <div class="review-info col-8 d-flex align-items-center">
        <div class="reviw-info-div">
          <h3 class="text-left">내 평점: {{review.score}}</h3>
          <div class="dummy-box">
          </div>
          <h5 class="text-left">{{ review.sentence }}</h5>
          <div class="dummy-box">
          </div>
          <div class="dummy-box">
          </div>
          <div class="button d-flex">
            <button class="glow-on-hover" @click="toMyReview">수정</button>
            <div class="dummy-box2">
            </div>
            <button class="glow-on-hover" @click="deleteReview">삭제</button>
          </div>
        </div>
      </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "MyReviewItems",
  props:{
    review: Object,
    user_id: Number
  },
  data() {
    return {
      submitData : {
        review: this.review,
        modal: true,
      },
    }
  },
  computed: {
    posterImg() {
      const imgurl = 'https://image.tmdb.org/t/p/w220_and_h330_face/' + this.review.movie.poster_path 
      return imgurl
    }
  },
  methods: {
    toMyReview() {
      console.log('리뷰 아이템',this.submitData)
      this.$emit('to-my-review', this.submitData)
    },
    deleteReview() {
      const API_URL ='http://127.0.0.1:8000'

      axios({
        method: 'delete',
        url: `${API_URL}/movies/${this.review.movie.id}/modify_myreview/${this.user_id}/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then(() => {
          this.$emit('renew-my-review')
        })
        .catch((err) => {
          console.log(err)
        })
    },

  }
}
</script>

<style scoped>
.dummy-box{
  height:50px
}
.dummy-box2{
  width: 10px;
}
.poster > img {
  max-width: 100%;
  height: auto;
}
.movie-title {
  position:relative;
  font-weight: bold;
  color: #f2f2f2;
}
.movie-rate p{
  position:relative;
  text-align:left;
}
.movie-overview p{
  position:relative;
  text-align:left;
}
.movie-overview h5{
  position:relative;
  text-align:left;
  font-weight: bold;
}
.text-left {
  text-align: left;
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