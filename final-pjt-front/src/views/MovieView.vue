<template>
  <div>
    <h1>Movie Page</h1>
    <hr>
    <MovieLists @to-movie-view="openModal"/>

    <!-- 컴포넌트 MyModal -->
    <ReviewModal @close="closeModal" v-if="modal">
      <!-- default 슬롯 콘텐츠 -->
      <p>영화의 리뷰를 입력해서 다른 영화를 추천 받아 보세요!</p>
      <div>
        <img :src="imgUrl" alt="">
      </div>
      <div><input v-model.trim="message"></div>
      <!-- /default -->
      <div>
        <star-rating v-model="score" :increment="0.5" :animate=true :glow=10></star-rating>
      </div>
      <!-- footer 슬롯 콘텐츠 -->
      <template slot="footer">
        <button @click="doSend">제출</button>
      </template>
      <!-- /footer -->
    </ReviewModal>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
import MovieLists from '@/components/MovieLists'
import ReviewModal from '@/components/ReviewModal'
// import router from '@/router'

export default {
    name : 'MovieView',
    components: {
        MovieLists,
        ReviewModal,
        StarRating,
    },
    data() {
      return {
        modal: false,
        message: '',
        movie : null,
        imgUrl: '',
        sendMessage: '',
        score: 0,
      }
    },
    methods: {
      openModal(submitData) {
        console.log(submitData)
        this.modal = submitData.modal
        this.movie = submitData.movie
        console.log(this.movie)
        this.imgUrl = 'https://image.tmdb.org/t/p/w220_and_h330_face/' + this.movie.poster_path
        
      },
      closeModal() {
        this.modal = false
        this.message = ''
      },
      getRecommendation() {
      
      },
      doSend() {
        if (this.message.length > 0) {
          alert(this.message)
          this.sendMessage = this.message
          this.message = ''

          const payload = {
          pk: this.movie.id,
          sentence: this.sendMessage,
          score: this.score*2,
          }
          
          console.log("제출할 때 넘겨 주는 데이터", payload)
          this.$store.dispatch('submitReview', payload)
          this.closeModal()
        } else {
          alert('메시지를 입력해주세요.')
        }

        // router.push({ name: 'RecommendView' })
      },
      // computed: {
      //   imgUrl() {
      //     const url = 'https://image.tmdb.org/t/p/w220_and_h330_face/' + this.movie.poster_path
      //     return url
      //   }
      // }
    }    
}
</script>

<style scoped>
h1 {
    font-size: 60px;
    color: linear-gradient(to right top, #000000, #ffffff);
    animation: gradient 10s ease infinite;
}
</style>