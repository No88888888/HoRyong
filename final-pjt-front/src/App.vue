<template>
  <body>
    <div id="app">
      <nav>
        <router-link :to="{ name: 'MovieView' }">Movies</router-link> | 
        <router-link :to="{ name: 'ProfileView' }">Profiles</router-link> | 
        <router-link :to="{ name: 'SignUpView' }">Sign Up Page</router-link> | 
        <router-link :to="{ name: 'LoginView' }">Login Page</router-link>
      </nav>
      <router-view/>

    </div>
  </body>
</template>

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

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
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
