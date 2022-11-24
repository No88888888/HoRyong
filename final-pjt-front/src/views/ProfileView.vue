<template>
  <div>
    <div class="dummy-box">
    </div>
    <div class="dummy-box">
    </div>
    <h3 class="fs-2"><b>내 프로필</b></h3>
    <div class="dummy-box">
    </div>
    <nav> 
      <router-link :to="{ name: 'MyReview' }">MyReview</router-link> |
      <router-link :to="{ name: 'WishList' }">WishList</router-link>
      <router-view/>
    </nav>
    <div class="dummy-box">
    </div>
  </div>
</template>

<script>
export default {
  name: "ProfileView"
}
</script>

<style>
nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #f2f2f2;
}

nav a.router-link-exact-active {
  color: yellow;
}
</style>