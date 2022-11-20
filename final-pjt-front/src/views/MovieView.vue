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
      <div><input v-model="message"></div>
      <!-- /default -->
      <!-- footer 슬롯 콘텐츠 -->
      <template slot="footer">
        <button @click="doSend">제출</button>
      </template>
      <!-- /footer -->
    </ReviewModal>
  </div>
</template>

<script>
import MovieLists from '@/components/MovieLists'
import ReviewModal from '@/components/ReviewModal'
export default {
    name : 'MovieView',
    components: {
        MovieLists,
        ReviewModal,
    },
    data() {
      return {
        modal: false,
        message: '',
        movie : null,
        imgUrl: '',
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
      },
      doSend() {
        if (this.message.length > 0) {
          alert(this.message)
          this.message = ''
          this.closeModal()
        } else {
          alert('메시지를 입력해주세요.')
        }
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

<style>
h1 {
    font-size: 60px;
    color: linear-gradient(to right top, #000000, #ffffff);
    animation: gradient 10s ease infinite;
}
</style>