<template>
<div>
  <div id="app">
    <nav-bar id="nav-bar"></nav-bar>
    <div class="body">
      <router-view/>
    </div>
  </div>
</div>
</template>

<script>
  import NavBar from '@/components/home/NavBar.vue'

  import { mapActions } from 'vuex'

  export default {
    name: 'App',
    components: { NavBar },
    methods: {
      ...mapActions(['getCurrentUser'])
    },
    created() {
      this.getCurrentUser()

    }
  }
</script>

<style>

/* html,body {
  width: 100%;
  height: 85vh;
} */

#app {
  /* background-color: black; */
  width: 100%;
  height: 100%;
  display:flex;
  flex-direction:column;
  justify-content: center;
  align-items:center;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;

}

#nav-bar {
  position: sticky;
  z-index:1;
  width: 100%;
  height:20%;
  top: 0;
}

/* body style */

.body {
  background-color:#040714;
  background-image:url(//cnbl-cdn.bamgrid.com/assets/4354a487f44fdc56c8f404b8b4a01f26c2a20dcc40bdb380da1b5c6cedef7d6e/original);
  width: 100%;
  height: 90%;
  padding: 50px;

  display: flex;
  flex-direction: column;
  justify-content: flex-start;

}

</style>
