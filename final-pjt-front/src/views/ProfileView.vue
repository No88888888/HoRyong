<template>
  <div>
    <nav> 
      <h1>Profile Page</h1>
      <router-link :to="{ name: 'MyReview' }">MyReview</router-link> | 
      <router-link :to="{ name: 'WishList' }">WishList</router-link>
      <router-view/>
    </nav>
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
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>