<template>
  <div>
    <h1>My Reviews</h1>
    <MyReviewItems
    class="review-items"
    v-for="review in reviews"
    :key="review.id"
    :review="review"
    :user_id="user_id"
    @to-my-review="openModal"
    @renew-my-review="getUserPk"
    />

    <ReviewModal @close="closeModal" v-if="modal">
      <p>내가 쓴 리뷰 수정하기</p>
      <div>
        <img :src="imgUrl" alt="">
      </div>
      <div><input class="form-control input-lg" v-model="sentence"></div>
      <div>
        <star-rating v-model="score" :increment="0.5" :animate=true :glow=10></star-rating>
      </div>
      <template slot="footer">
        <button @click="doSend">모달에서 수정하기</button>
      </template>
    </ReviewModal>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
import MyReviewItems from '@/components/MyReviewItems'
import ReviewModal from '@/components/ReviewModal'
import axios from 'axios'


const API_URL = 'http://127.0.0.1:8000'

export default {
  name : "MyReviews",
  components: {
    MyReviewItems,
    ReviewModal,
    StarRating,
  },
  data() {
    return {
      user_id : null,
      reviews: [],
      username: null,
      // 모달에 넣을 데이터들
      movie : null,
      imgUrl : null,
      modal : false,
      score : 0,
      // 수정 보낼 데이터들
      sentence: null,
    }
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
          this.username = res.data.username
          return {'user_id': res.data.pk}
        })
        .then((res) => {
          const user_id = res.user_id
          axios({
            method: 'get',
            url: `${API_URL}/movies/my_review/${user_id}/`,
            data: {
              user_pk: user_id,
            },
            headers: {
              Authorization: `Token ${ this.$store.state.token }`
            }
          })
            .then((res) => {
              this.reviews = res.data
            })
        })
    },

    openModal(submitData) {
        console.log("리뷰 모달에 넘길 데이터",submitData)
        this.modal = submitData.modal
        this.movie = submitData.review.movie
        this.sentence = submitData.review.sentence
        this.score = submitData.review.score
        this.imgUrl = 'https://image.tmdb.org/t/p/w220_and_h330_face/' + submitData.review.movie.poster_path
    },
    closeModal() {
      this.modal = false
      this.message = ''
    },
    getRecommendation() {
    
    },
    doSend() {
      if (this.sentence.length > 0) {
        alert('리뷰가 수정되었습니다.')
        this.fixReview = this.sentence
        this.closeModal()
      } else {
        alert('메시지를 입력해주세요.')
      }
      const payload = {
        pk: this.movie.id,
        sentence: this.fixReview,
        score: this.score*2,
      }
      console.log("수정 제출할 때 넘겨 주는 데이터", payload)
      // this.$store.dispatch('changeReview', payload)
      // router.push({ name: 'MyReview' })
    },
  }
}
</script>

<style>
input {
  width:200px;
  height:100px;
  font-size:20px;
}
</style>