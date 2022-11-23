<template>
  <div>
    <h3>WishListItems</h3>
    <h3>{{wishlists.id}}</h3>
  </div>
</template>

<script>
export default {
  name : "WishListItems",
  props : {
    wishlist : Array,
  },
  data() {
    return {
      wishlists : this.wishlist,
    }
  }
}
</script>

<style>

</style>