<template>
  <body>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css">
    <div id="app">
      <nav id="navbar" class="navbar navbar-expand-lg navbar-light navbar-fixed-top">
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <!-- 아이콘으로 링크 보내기 -->
        <router-link id="Icon" class="navbar-brand" :to="{ name: 'MovieView' }">HoRyong</router-link>
          <div class="collapse navbar-collapse d-flex justify-content-between" id="navbarTogglerDemo03">
            
            <div class="form-inline my-2 my-lg-0">
            </div>

            <ul class="navbar-nav mr-auto mt-2 mt-lg-0 d-flex justify-content-end">
              <li id="liTag" class="nav-item active">
                <router-link class="nav-item " :to="{ name: 'MovieView' }">Movies</router-link>
              </li>
              <li id="liTag" class="nav-item">
                <router-link class="nav-item" :to="{ name: 'ProfileView' }" v-show="isLogedIn">Profiles</router-link>
                <router-link class="nav-item" :to="{ name: 'SignUpView' }" v-if="!isLogedIn">Sign Up</router-link> 
              </li>
              <li id="liTag" class="nav-item">
                <a class="nav-item" v-show="isLogedIn" @click.prevent="logOut">Logout</a>
                <router-link class="nav-item" :to="{ name: 'LoginView' }" v-if="!isLogedIn">Login</router-link>
              </li>
            </ul>
          </div>
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

<style scopd>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css");
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffffff;
}

nav {
  padding: 30px;
  z-index: 1;
}

#navbar {
  position: absolute;
  /* overflow: hidden; */
  background-color: none;
  opacity: 1;
}

#Icon {
  display: block;
  color: #f2f2f2;
  text-align: center;
  padding: 10px;
  text-decoration: none;
  font-weight: bold;
}

#liTag > a {
  display: block;
  color: #f2f2f2;
  text-align: center;
  padding: 10px;
  text-decoration: none;
  font-weight: bold;
}

#liTag > a.router-link-exact-active {
  color: #42b983;
}
#liTag > a.exact-active {
  color: #42b983;
}

.navbar-nav {
  width: 30% !important;

}

/* .content {
  padding: 16px;
}

.sticky {
  position: fixed;
  top: 0;
  width: 100%;
}
.sticky + .content {
  padding-top: 60px;
} */

body {
	background: linear-gradient(-45deg, #ffffff, #000000, #ffffff, #000000);
	background-size: 400% 400%;
	animation: gradient 10s ease infinite;
	height: 100vh;
}

/* @keyframes gradient {
	0% {
		background-position: 0% 50%;
	}
	50% {
		background-position: 100% 50%;
	}
	100% {
		background-position: 0% 50%;
	}
} */

</style>
