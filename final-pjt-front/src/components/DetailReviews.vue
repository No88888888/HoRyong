<template>
  <div class="container1">
    <div class="container2">
      <span id="review"><p class="text-left">익명의 사용자{{getIndex}} :{{ review.sentence }}</p>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DetailReviews',
  props: {
    review: Object,
    index: Number,
  },
  computed:{
    getIndex() {
      return this.index + 1
    }
  },
}
</script>

<style scoped>
/* #review {
  text-align: left;
} */
</style>