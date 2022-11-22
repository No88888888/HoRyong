<template>
  <div>
    <h1>Recommend Page</h1>
    <div>
      <h2>{{ username }} 님이 작성하신 리뷰의 키워드는</h2>
      <b><h2>"{{ firstMovie.keyword }}"입니다.</h2></b>
      <h2>해당 키워드로 추천 드릴 영화는</h2>
      <h3>"{{ firstMovie.movie.title }}" 입니다.</h3>
      <img :src="firstMovieImg" alt="">
      <div>
        <h2>{{ username }} 님의 다른 키워드</h2>
      </div>
      <div>
        <span>두번 째 키워드: <div @click="changeToSecond">{{ secondMovie.keyword }}</div></span>
      </div>
      <div>
        <span>세번 째 키워드: <div @click="changeToThird">{{ thirdMovie.keyword }}</div></span>
      </div>
    </div>

  </div>
</template>

<script>

export default {
  name: 'RecommendView',
  data() {
    return {
      movie : this.$store.state.recommendMovie
    }
  },
  computed: {
    firstMovie() {
      return this.$store.state.recommendMovie[0]
    },
    username() {
      console.log(this.$store.state.username)
      return this.$store.state.username
    },
    firstMovieImg(){
      return 'https://image.tmdb.org/t/p/w220_and_h330_face/'+ this.$store.state.recommendMovie[0].movie.poster_path
    },
    secondMovie() {
      return this.$store.state.recommendMovie[1]
    },
    thirdMovie() {
      return this.$store.state.recommendMovie[2]
    }
  },
  methods: {
    changeToSecond() {
      this.$store.dispatch('switchWithSecond')
      this.$router.push({ name: 'RecommendView'})
      this.$router.go()
    },
    changeToThird() {
      this.$store.dispatch('switchWithThird')
      this.$router.push({ name: 'RecommendView'})
      this.$router.go()
    }
  }
}
</script>

<style>

</style>