import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView'
import ProfileView from '@/views/ProfileView'
import MyReview from '@/components/MyReview'
import WishList from '@/components/WishList'
import DetailView from '@/views/DetailView'
import SignUpView from '@/views/SignUpView'
import LoginView from '@/views/LoginView'
import RecommendView from '@/views/RecommendView'
import store from '@/store/index.js'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/profile',
    name: 'ProfileView',
    component: ProfileView,
    children : [
      {
        path: '/myreview',
        name: 'MyReview',
        component: MyReview,
        meta: {authRequired: true},
      },
      {
        path: '/wishlist',
        name: 'WishList',
        component: WishList,
        meta: {authRequired: true},
      }
    ],
    meta: {authRequired: true},
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView,
    beforeEnter(to, from, next) {
      console.log('비포 엔터',store.state.username)
      if(store.state.username) {
        alert('이미 로그인이 되어있습니다.')
        next({ name: 'MovieView'})
      } else {
        next()
      }
    }
  },  
  {
    path: '/recommend',
    name: 'RecommendView',
    component: RecommendView,
  },
  {
    path: '/:id',
    name: 'DetailView',
    component: DetailView,
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// router.beforeEach((to, from, next) => {
//   // 접근 가능 여부(로그인 상태면 true, 비로그인 상태면 false)
//   const authenticationState = store?.state?.token? true : false

//   console.log('to', to)
//   // 이동할 사이트가 인증을 필요로 하는 사이트인 경우
//   const authentication = ['SignUpView', 'LoginView'].includes(to.name)? false: true

//   console.log('authenticationState', authenticationState)
//   console.log('authentication', authentication)

//   console.log('From To',from, to)
//   // 비로그인 상태 && 이동하려는(이동할) 사이트가 로그인 해야만 하는 사이트인 경우 
//   if (!authenticationState && authentication) {
//     next({name: 'LoginView'})
//   }
//   else {
//     next()
//   }
// })

export default router
