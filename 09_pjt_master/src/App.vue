<template>
  <div id="app" :style="{'background-image':'url(https://img1.daumcdn.net/thumb/R300x0/?fname=https://k.kakaocdn.net/dn/yBAjB/btrHpozmha7/M0aMznMXD5H9VNfzmaPk80/img.gif)'}" style="height:100vh background-repeat:no-repeat">

  <!-- <div id="app" :style="{'background-image':'url(./assets/ssafy_logo.png)'}"> -->
  <nav id="navbar-example2" class="navbar px-3 mb-3" style="background-color: #e3f2fd;">
    <img @click="GoHome" src="./assets/ssafy_logo.png" alt="" style="width:40px" class="col-1">
      <ul class="nav nav-pills">
        <li class="nav-item">
          <router-link to="/movies" style="text-decoration:none;">Movie</router-link> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        </li>
        <li class="nav-item">
          <router-link to="/random" style="text-decoration:none;">Random</router-link> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        </li>
        <li class="nav-item">
          <router-link to="/watch-list" style="text-decoration:none;">WatchList</router-link>
        </li>
    </ul>
  </nav>

    <router-view/>
  </div>
</template>

<script>

export default{
  name:'App',
  methods: {
    GoHome() {
      this.$router.push({name:'HomeView'})
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

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}


</style>

