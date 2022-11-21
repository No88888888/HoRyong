<template>
  <div>
    <h1>Recommend Page</h1>
    <div>
      <!-- <RecommendItem/> -->
      <h2>{{ username }}</h2>
      <h2>님이 작성하신 리뷰의 키워드는</h2>
      <h2>{{ keyword }}입니다.</h2>
    </div>

    <div>

    </div>
  </div>
</template>

<script>
// import RecommendItem from '@/components/RecommendItem';

export default {
  name: 'RecommendView',
  components: {
    // RecommendItem,
  },
  computed: {
    recommendMovie() {
      return this.$store.state.recommendMovie
    },
    username() {
      console.log(this.$store.state.username)
      return this.$store.state.username
    },
  },
  methods:{
  }
}
</script>

<style>

</style>