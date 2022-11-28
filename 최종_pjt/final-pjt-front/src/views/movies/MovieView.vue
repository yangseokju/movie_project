<template>
  <div id="movie_view">
    <div class="input d-flex justify-content-between align-items-start" style="width: 60%">
        <input type="text" class="form-control my-3" @input="searchMovies($event.target.value)" @keyup.enter="searchMovies(query)"> &nbsp;&nbsp;&nbsp;
    </div>
    <div v-if="searchedMovies.length===0">
        <div class="row row-cols-1 row-cols-xl-5 row-cols-md-4 row-cols-sm-2 g-4 m-auto" style="width:80%;">
            <MovieCard
            v-for="movie in movies"
            :key="movie.id"
            :movie="movie"
            />
        </div>
    </div>
    <div v-else>
        <div class="row row-cols-1 row-cols-xl-5 row-cols-md-4 row-cols-sm-2 g-4 m-auto" style="width:80%;">
            <MovieCard
            v-for="movie in searchedMovies"
            :key="movie.id"
            :movie="movie"
            />
        </div>
    </div>
  </div>
  </template>
  
  <script>
    import { mapGetters, mapActions } from 'vuex'
    import MovieCard from '@/components/MovieCard'

    export default {
        name: 'MovieView',
        components: {MovieCard},
        data(){
            return {
                // query: '',
            }
        },
        computed: {
            ...mapGetters(['movies','searchedMovies'])
        },
        methods: {
            ...mapActions(['getMovies','searchMovies']),
        },
        created(){
            this.getMovies()
        },
    }

  </script>
  
  <style>
  #movie_view {
    min-height:100vh;
    height:100%;
  }
  </style>
