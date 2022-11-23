<template>
  <div>
    <h3>{{ this.wishMovie }}</h3>
  </div>
</template>

<script>
export default {
  name: 'WishListDetail',
  props: {
    toWishDetail: Object,
  },
  computed: {
    wishDetail() {
      console.log('왔나요?', this.toWishDetail)
      return this.toWishDetail
    }
  }
}
</script>

<style>

</style>