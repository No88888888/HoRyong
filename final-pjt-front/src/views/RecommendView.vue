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
        <p>두번 째 키워드: <a href="">"{{ secondMovie.keyword }}" </a></p>
      </div>
      <div>
        <p>세번 째 키워드: <a href="">"{{ thirdMovie.keyword }}" </a></p>
      </div>
    </div>

    <div>
      <h1>저장 확인</h1>
      <h2>{{ movie }}</h2>
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
}
</script>

<style>

</style>