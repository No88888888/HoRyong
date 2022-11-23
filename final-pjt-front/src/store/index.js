import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    movies: [],
    token: null,
    recommendMovie: null,
    username: null,
    watchedMovie: null,
    wishlist: [],
    myReviewList:[],
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    // 회원가입 && 로그인
    SAVE_TOKEN(state, token) {
      state.token = token
    },
    RECOMMEND_MOVIE(state, recommendation) {
      state.recommendMovie = recommendation
    },
    WISHLIST_MOVIE(state, mywishlist) {
      state.wishlist = mywishlist
    },
    SWITCH_SECOND(state) {
      const temp = state.recommendMovie[0]
      state.recommendMovie[0] = state.recommendMovie[1]
      state.recommendMovie[1] = temp
    },
    SWITCH_THIRD(state) {
      const temp = state.recommendMovie[0]
      state.recommendMovie[0] = state.recommendMovie[2]
      state.recommendMovie[2] = temp     
    },
    SAVE_WATCHED(state, data) {
      state.watchedMovie = data
    },
    DELETE_ALL(state) {
      state.movies = [],
      state.token = null,
      state.recommendMovie = null,
      state.username = null,
      state.watchedMovie = null
    },
    GET_MY_REVIEWS(state,data) {
      state.myReviewList = data
    }
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
      })
        .then((res) => {
          context.commit('GET_MOVIES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
          context.state.username = payload.username
        })
        .then(() => {
          router.push({ name: 'MovieView' })
        })
    },
    login(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        },
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
          context.state.username = payload.username
        })
        .then(() => {
          axios({
            method: 'get',
            url: `${API_URL}/movies/get_watched_movie/`,
            headers: {
              Authorization: `Token ${context.state.token}`
            }
          })
          .then((res) => {
            console.log(res.data)
            context.commit('SAVE_WATCHED', res.data)
          })
          .then(() => {
            router.push({ name: 'MovieView' })
          })
        })
    },
    logout(context) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          context.commit('DELETE_ALL')
          router.go()
        })
    },
    submitReview(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/movies/${payload.pk}/create_review/`,
        data: {
          movie_pk: payload.pk,
          sentence: payload.sentence,
          score: payload.score,
        },
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) =>{
          console.log("리뷰 제출 데이터", res.data)
          context.commit('RECOMMEND_MOVIE', res.data)
        })
        .then(() => {
          router.push({ name: 'RecommendView' })
        })
    },
    // submitWishList(context, payload) {
    //   axios({
    //     method: 'post',
    //     url: `${API_URL}/movies/${payload.movie_id}/modify_wishlist/${payload.pk}/`,
    //     data: {
    //       movie_pk: payload.movie_id,
    //     },
    //     headers: {
    //       Authorization: `Token ${context.state.token}`
    //     }
    //   })
    //     .then((res) =>{
    //       console.log("위시리스트 제출 데이터", res.data)
    //       context.commit('WISHLIST_MOVIE', res.data) 
    //   })
    // },
    getMyReviews(context) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          const user_pk = res.data.pk
          this.username = res.data.username
          axios({
            method: 'get',
            url: `${API_URL}/movies/my_review/${user_pk}/`,
            headers: {
              Authorization: `Token ${context.state.token}`
            }
          })
          .then((res) => {
            console.log('GET_MY_REVIEWS',res.data)
            context.commit('GET_MY_REVIEWS',res.data)
          })
        })

    },
    switchWithSecond(context) {
      context.commit('SWITCH_SECOND')
    },
    switchWithThird(context) {
      context.commit('SWITCH_THIRD')
    },
    saveWatchedMovie(context, data) {
      context.commit('SAVE_WATCHED', data)
    },
    saveWishList(context, data) {
      context.commit('WISHLIST_MOVIE', data)
    }
  },
  modules: {
  }
})
