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
        <star-rating id="star" v-model="score" :increment="0.5" :animate=true :glow=10 active-color="#black"></star-rating>
      </div>
      <template slot="footer">
        <button class="glow-on-hover" @click="doSend">모달에서 수정하기</button>
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
        // this.score = submitData.review.score
        this.imgUrl = 'https://image.tmdb.org/t/p/w220_and_h330_face/' + submitData.review.movie.poster_path
    },
    closeModal() {
      this.modal = false
      this.message = ''
    },
    doSend() {
      if (this.sentence.length > 0) {
        alert('리뷰가 수정되었습니다.')
        this.closeModal()
      } else {
        alert('메시지를 입력해주세요.')
      }
  
      const API_URL ='http://127.0.0.1:8000'
      axios({
        method: 'put',
        url: `${API_URL}/movies/${this.movie.id}/modify_myreview/${this.user_id}/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
        data: {
          sentence : this.sentence,
          score : this.score*2,
          movie_id : this.movie_id,
          user_id : this.user_id,
        }
      })
        .then(() => {
          this.getUserPk()
        })
        .catch((err) => {
          console.log(err)
        })
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
#star {
  color:white;
  display: flex;
  justify-content: center;
  /* align-items: center; */
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