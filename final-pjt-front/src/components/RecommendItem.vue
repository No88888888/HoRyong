<template>
  <div>
    <h3>추천 영화</h3>
    <h1 :v-show="recoMovie"> ha ha </h1>
  </div>  
</template>

<script>
export default {
  name: "RecommendItem",
  computed: {
    recoMovie() {
      return this.$store.state.recommendMovie
    }
  }

}
</script>

<style>

</style>