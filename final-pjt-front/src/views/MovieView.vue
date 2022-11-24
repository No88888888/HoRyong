<template>
  <div>
    <div class="dummy-box">
    </div>
    <div class="dummy-box">
    </div>
    <h3 class="fs-2"><b>KeyMoo</b></h3>
    <div class="dummy-box">
    </div>
    <div class="dummy-box">
    </div>
    
    <MovieLists @to-movie-view="openModal"/>


    <!-- 컴포넌트 MyModal -->
    <ReviewModal @close="closeModal" v-if="modal">
      <!-- default 슬롯 콘텐츠 -->
      <p id="modal-title">영화의 리뷰를 입력해서 다른 영화를 추천 받아 보세요!</p>
      <div>
        <img :src="imgUrl" alt="">
      </div>
      <br>
      <span class="input">
        <input v-model="message">
        <span></span>
      </span>
      <br>
      <!-- /default -->
      <div id="star">
        <star-rating v-model="score" :increment="0.5" :animate=true :glow=10 active-color="#black"></star-rating>
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

<style lang="scss" scoped>
h1 {
    font-size: 60px;
    color: linear-gradient(to right top, #000000, #ffffff);
    animation: gradient 10s ease infinite;
}
input {
  width: 400px;
}
#star {
  color:white;
  display: flex;
  justify-content: center;
  /* align-items: center; */
  
}
p {
  color: white;
}
.input {
  
  // needs to be relative so the :focus span is positioned correctly
  position:relative;
  
  // bigger font size for demo purposes
  // font-size: 1.5em;
  
  // the border gradient
  background: linear-gradient(21deg, #000000, #646464);
  
  // the width of the input border
  padding: 3px;
  
  // we want inline fields by default
  display: inline-block;
  
  // we want rounded corners no matter the size of the field
  border-radius: 0.2em;
  
  // style of the actual input field
  *:not(span) {
    position: relative;
    display: inherit;
    border-radius: inherit;
    margin: 0;
    border: none;
    outline: none;
    padding: 2 .325em;
    z-index: 1; // needs to be above the :focus span
    
    // summon fancy shadow styles when focussed
    &:focus + span {
      opacity: 1;
      transform: scale(1);
    }
  }
  
  // we don't animate box-shadow directly as that can't be done on the GPU, only animate opacity and transform for high performance animations.
  span {
    
    transform: scale(.993, .94); // scale it down just a little bit
    transition: transform .5s, opacity .25s;
    opacity: 0; // is hidden by default
    
    position:absolute;
    z-index: 0; // needs to be below the field (would block input otherwise)
    margin:4px; // a bit bigger than .input padding, this prevents background color pixels shining through
    left:0;
    top:0;
    right:0;
    bottom:0;
    border-radius: inherit;
    pointer-events: none; // this allows the user to click through this element, as the shadow is rather wide it might overlap with other fields and we don't want to block those.
    
    // fancy shadow styles
    box-shadow: inset 0 0 0 3px #fff,
      0 0 0 4px #fff,
      3px -3px 30px #000000, 
      -3px 3px 30px #646464;
  }
}
.dummy-box{
  height:50px
}
</style>