<template>
    <div>
        <div class="card h-100 col movie-item" @click="movie_detail">
            <img :src="movie.poster_path" class="card-img-top" alt="..." style="height:100%; width:100%">
        </div>
    </div>
</template>

<script>

export default {
    name:'MovieCard',
    props: {
        'movie':Object,
    },
    methods: {
        movie_detail() {
            this.$store.dispatch('getMovieDetail',this.movie.id)
            this.$router.push({name:'moviesDetail', params:{movie_pk:`${this.movie.id}`}})
        }
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
