<template>
  <div>
    <div class="container">
      <div>
        <img :src="posterImg" alt="" class="">
        <h5>{{ review.movie.title }}</h5>
      </div>
      <p>내 평점: {{review.score}}</p>
      <h5>{{ review.sentence }}</h5>
      <button @click="toMyReview">수정</button>
      <button @click="deleteReview">삭제</button>
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

<style>

</style>