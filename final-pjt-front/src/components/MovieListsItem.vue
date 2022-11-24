<template>
  <div >
    <div>
    <div class="container">
      <img :src="posterImg" alt="" class="image" v-bind:class="{'selected': isSelected}">
      <div class="zoom">
        <div>
          <router-link :to="{ name: 'DetailView', params: { id: movie.id } }">
            <button class="glow-on-hover" type="button">GET DETAIL</button>
          </router-link>
        </div>
        <br>
        <div>
          <button class="glow-on-hover" type="button" v-if="isSelected" @click="toMovieList">리뷰 작성</button>
        </div>
      </div>
    </div>
    <h5>{{ movie.title }}</h5>
  </div>
  <button class="glow-on-hover" type="button" v-if="isLogedIn" @click="watchedMovie">Watched</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name : 'MovieListsItem',
  props: {
      movie: Object,
  },
  data() {
    return {
      submitData : {
        movie: this.movie,
        modal: true,
      },
      isSelected: false
    }
  },
  computed: {
    posterImg() {
      const imgurl = 'https://image.tmdb.org/t/p/w220_and_h330_face/' + this.movie.poster_path 
      return imgurl
    },
    isLogedIn() {
      return this.$store.state.username
    },
    watchedMovieList() {
      return this.$store.state.watchedMovie
    },
    myReviewList() {
      const myReviewitems = this.$store.state.myReviewList
      let myReviews = []
      myReviewitems.forEach((myReview) => {
        myReviews.push(myReview.movie.id)
      })
      return myReviews
    },
  },
  methods: {
    toMovieList() {
      if (this.myReviewList?.includes(this.movie.id)) {
        alert('이미 리뷰를 작성 하셨습니다.')
        this.$router.push({ name: 'MyReview' })
      } else {
        this.$emit('to-movie-list', this.submitData)
      }
    },
    watchedMovie() {
      const API_URL =`http://127.0.0.1:8000/movies/${this.movie.id}/watched_movie/`
      axios({
        method: 'post',
        url: API_URL,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) =>{
        this.$store.dispatch('saveWatchedMovie', res.data)
        return res
      })
      .then(() => {
        this.watchedOrNot()
      })
    },
    // 여기서 부터 태그 관련 함수
    watchedOrNot() {
      if (this.watchedMovieList?.includes(this.movie.id)) {
        this.isSelected = true
      } else {
        this.isSelected = false
      }
    },
  },
  created() {
    this.watchedOrNot()
  },
}

</script>

<style scoped>

.selected {
  padding:4px;
  position: relative;
  width: 100%;
  height: 100%;
  background-color: none;
  border: 3px solid transparent;
  border-image: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
  border-image-slice: 1;
}
.container {
  position: relative;
  align-content: center;
}

.image {
  opacity: 1;
  display: block;
  transition: .5s ease;
  backface-visibility: hidden;
}

.zoom {
  transition: .5s ease;
  opacity: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  text-align: center;
}

.container:hover .image {
  opacity: 0.3;
  filter: blur(4px);
}

.container:hover .zoom {
  opacity: 1;
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

