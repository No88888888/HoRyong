import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import Carousel3d from 'vue-carousel-3d'

Vue.use(BootstrapVue)
Vue.config.productionTip = false
Vue.use(Carousel3d)

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
