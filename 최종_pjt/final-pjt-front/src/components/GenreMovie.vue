<template>
  <div>
    <div v-if="genre_movies.length!==0">
      <div class="row row-cols-1 row-cols-xl-5 row-cols-md-2 row-cols-sm-2 g-4 m-auto" style="width:80%;">  
        <div v-for="movie in genre_movies" :key="movie.id">
          <div>
            <div class="card h-100 col movie-item" @click="movie_detail(movie)">
              <img :src="movie.poster_path" class="card-img-top" alt="..." style="height:100%; width:100%">
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else style="height:100vh; color:white">
      선택된 장르가 없습니다.&nbsp;&nbsp;
      <router-link to='/' style="text-decoration:none">장르선택으로 이동하기</router-link>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    name:'GenreMovie',
    methods: {
      movie_detail(movie) {
          this.$store.dispatch('getMovieDetail',movie.id)
          this.$router.push({name:'moviesDetail', params:{movie_pk:movie.id}})
      },
    },
    computed: {
      ...mapGetters(['genre_movies'])
    },
  }
</script>

<style>

.cardpoint {
  overflow:hidden;
  line-height: 2rem;
  max-height: 15rem;
  -webkit-box-orient: vertical;
  display: block;
  display: -webkit-box;
  overflow: hidden !important;
  text-overflow: ellipsis;
  -webkit-line-clamp: 6;
}

.movie-item {
  position: relative;
  display: block;
  flex: 1 1 0px;
  transition: transform 500ms;
}

.movie-item:focus,

.movie-item:hover {
  transform: scale(1.4);
  z-index: 1;
}

</style>
