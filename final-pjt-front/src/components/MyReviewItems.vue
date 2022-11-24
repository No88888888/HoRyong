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
            <h5>{{ review.movie.title }}</h5>
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
          <div class="button d-flex justify-content-between">
            <button @click="toMyReview">수정</button>
            <button @click="deleteReview">삭제</button>
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
.poster > img {
  max-width: 100%;
  height: auto;
}
.movie-title h2{
  position:relative;
  text-align:left;
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
</style>