<template>
  <div class="home">
    <h1 style="color:white">원하는 장르를 선택해주세요 !</h1>
    <div class="row row-cols-4 g-4 m-auto button-list">
      <button @click="genre_pick" class="btn avtive test" :class="{'picked':pick_check('28')}" value=28>액 션</button>&nbsp;&nbsp;&nbsp;
      <button @click="genre_pick" class="btn avtive test" :class="{'picked':pick_check('12')}" value=12>모 험</button>&nbsp;&nbsp;&nbsp;
      <button @click="genre_pick" class="btn avtive test" :class="{'picked':pick_check('16')}" value=16>애니메이션</button>&nbsp;&nbsp;&nbsp;
      <button @click="genre_pick" class="btn avtive test" :class="{'picked':pick_check('35')}" value=35>코미디</button>&nbsp;&nbsp;&nbsp;
      <button @click="genre_pick" class="btn avtive test" :class="{'picked':pick_check('80')}" value=80>범 죄</button>&nbsp;&nbsp;&nbsp;
      <button @click="genre_pick" class="btn avtive test" :class="{'picked':pick_check('99')}" value=99>다큐멘터리</button>&nbsp;&nbsp;&nbsp;
      <button @click="genre_pick" class="btn avtive test" :class="{'picked':pick_check('18')}" value=18>드라마</button>&nbsp;&nbsp;&nbsp;
      <button @click="genre_pick" class="btn avtive test" :class="{'picked':pick_check('10751')}" value=10751>가 족</button>&nbsp;&nbsp;&nbsp;
      <button @click="genre_pick" class="btn avtive test" :class="{'picked':pick_check('14')}" value=14>판타지</button>&nbsp;&nbsp;&nbsp;
      <button @click="genre_pick" class="btn avtive test" :class="{'picked':pick_check('36')}" value=36>역 사</button>&nbsp;&nbsp;&nbsp;
      <button @click="genre_pick" class="btn avtive test" :class="{'picked':pick_check('27')}" value=27>공 포</button>&nbsp;&nbsp;&nbsp;
      <button @click="genre_pick" class="btn avtive test" :class="{'picked':pick_check('10402')}" value=10402>음 악</button>&nbsp;&nbsp;&nbsp;
      <button @click="genre_pick" class="btn avtive test" :class="{'picked':pick_check('9648')}" value=9648>미스테리</button>&nbsp;&nbsp;&nbsp;
      <button @click="genre_pick" class="btn avtive test" :class="{'picked':pick_check('10749')}" value=10749>로맨스</button>&nbsp;&nbsp;&nbsp;
      <button @click="genre_pick" class="btn avtive test" :class="{'picked':pick_check('878')}" value=878>S F</button>&nbsp;&nbsp;&nbsp;
      <button @click="genre_pick" class="btn avtive test" :class="{'picked':pick_check('10770')}" value=10770>TV 영화</button>&nbsp;&nbsp;&nbsp;
      <button @click="genre_pick" class="btn avtive test" :class="{'picked':pick_check('53')}" value=53>스릴러</button>&nbsp;&nbsp;&nbsp;
      <button @click="genre_pick" class="btn avtive test" :class="{'picked':pick_check('10752')}" value=10752>전 쟁</button>&nbsp;&nbsp;&nbsp;
      <!-- <button @click="genre_pick" class="btn avtive test" :class="{'picked':pick_check('37')}" value=37>서 부</button> -->
    </div>
    <br>
    <br>
    <div>
      <button @click="go_genre" class="btn btn-icon">영화보러가기!</button>
    </div>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'

  export default {
      name: 'HomeView',
      components: {},
      data() {
          return {
            pick_movie:[],
            select_movie:[],
            search_value:"",
          }
      },
      computed: {
        ...mapGetters(['movies',]),
      },
      methods: {
          ...mapActions(['getMovies',]),
          genre_pick(event) {
            this.select_movie = []
            if (this.pick_movie.includes(event.target.value)) {
              this.pick_movie.splice(this.pick_movie.indexOf(event.target.value), 1)
            }
            else {
              this.pick_movie.push(event.target.value)
            }
            this.movies.forEach((movie) => {
              for (const genre of this.pick_movie) {
                if (movie.genre.includes(Number(genre))) {
                  this.select_movie.push(movie)
                  break
                }
              }
            })
            // console.log(this.select_movie)
            this.$store.dispatch('genre_movie',this.select_movie)
          },
          pick_check(checked) {
            if (this.pick_movie.includes(checked)) {
              return true
            } else {
              return false
            }
          },
          go_genre() {
            if (this.pick_movie.length === 0) {
              alert('영화를 선택해주세요!')
            } else {
              this.$router.push({name:'GenreMovie'})
            }
          }
        },
      created(){
          this.getMovies()
      },
  }

</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

.test {
  width:120px;
  height:50px;
  font-size:20px !important;
  border:2px solid white !important;
  color:white !important;
  vertical-align: middle;
  display: table-cell;
  margin:auto;
}

.btn-icon { 
  margin-right: 17px;
  width:271px; 
  height:60px;
  font-size:24px !important;
  border:2px solid blue !important;
  color:blue !important;
}

.home {
  height:100vh;
  align-content: center;
  width: 60%;
  font-family: 'Jua', sans-serif;
}

.test:hover, .test:active {
  background-color:#0D6EFD;
}

.btn-icon:hover, .btn-icon:active {
  background-color: blue;
  color:black !important;
  /* border : 2px solid black !important; */
}

.picked {
  background-color: blue !important;
}
</style>