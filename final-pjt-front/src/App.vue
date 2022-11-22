<template>
  <body>
    <div id="app">
      <nav>
          <router-link :to="{ name: 'MovieView' }">Movies</router-link>
          <router-link :to="{ name: 'ProfileView' }" v-show="isLogedIn">Profiles</router-link>
          <a v-show="isLogedIn" @click.prevent="logOut">Logout</a>
          <router-link :to="{ name: 'SignUpView' }" v-show="!isLogedIn">Sign Up</router-link> 
          <router-link :to="{ name: 'LoginView' }" v-show="!isLogedIn">Login</router-link>
          <router-link :to="{ name: 'RecommendView' }">Recommend</router-link>
      </nav>
      <router-view/>

    </div>
  </body>
</template>
<script>
export default {
  name : "App",
  computed: {
    isLogedIn() {
      return this.$store.state.username
    }
  },
  methods: {
    logOut() {
      this.$store.dispatch('logout')
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a-exact-active {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

nav a.exact-active {
  color: #42b983;
}

body {
	background: linear-gradient(-45deg, #ffffff, #000000, #ffffff, #000000);
	background-size: 400% 400%;
	animation: gradient 10s ease infinite;
	height: 100vh;
}

@keyframes gradient {
	0% {
		background-position: 0% 50%;
	}
	50% {
		background-position: 100% 50%;
	}
	100% {
		background-position: 0% 50%;
	}
}

</style>
