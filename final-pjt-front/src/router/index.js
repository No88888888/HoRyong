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
        component: MyReview
      },
      {
        path: '/wishlist',
        name: 'WishList',
        component: WishList
      }
    ],
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/:id',
    name: 'DetailView',
    component: DetailView,
  },
  {
    path: '/recommend',
    name: 'RecommendView',
    component: RecommendView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
