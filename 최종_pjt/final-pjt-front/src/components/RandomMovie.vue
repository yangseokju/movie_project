<template>
  <div v-if="random_movies">
    <div class="wrapper card h-100 col row g-4" :style="{'background-image':`url(${random_movies.backdrop_path})`}">
      <div class="container p-3 mt-3">
        <div class="container neumorph p-5">
          <div>
            <button type="button" class="btn btn btn-primary mb-2 mt-3" style="height: 40px; width:300px;" @click="RandomMovie">랜덤영화</button>
          </div>
          <div class="detail p-3 neumorph3">
            <div class="row">
              <h2><b>{{ random_movies.title }}</b></h2>
              <div class="col-12 col-lg-4 align-items-center p-3">
                <img :src="random_movies.poster_path" alt="" class="img-fluid">
              </div>
              <div class="col-12 col-lg-8 p-3">
                <div class="description mx-3 mt-3">
                <h6 class="my-3"><b>{{ random_movies.release_date }} 개봉</b></h6>
                <h6 class="my-3"><b>장르 :
                <span v-for="(genre, index) in random_movies.genre" :key="index">
                  {{ genre.name }}
                </span></b></h6>
                <h6 class="my-3"><b>평점 : {{ random_movies.vote_avg }}</b></h6>
                <div>
                  <span v-if="random_movies.overview !==''">
                    {{ random_movies.overview }}
                  </span>
                  <span v-if="random_movies.overview ===''">
                    영화소개가 없습니다😢
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
// import random_movie from '@/store/modules/random_movie'
import { mapGetters } from 'vuex'
import _ from 'lodash'

export default {
    name : 'RandomMovie',
    methods: {
        RandomMovie() {
          const movie_pk = _.random(1, 1000)
          this.$store.dispatch('random_Movies', movie_pk)
        },
    },

    computed: {
            ...mapGetters(['random_movies'])
    },
    created() {
      this.RandomMovie()
    }
}

</script>

<style>
  .fade-enter-from,
  .fade-enter-to {
    opacity: 0;
  }
  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.5s ease-out;
  }
  .description {
    font-family: 'Nanum Gothic', sans-serif;
  }

  .wrapper {
  /* width: 500px;*/
  /* display: flex; */
  border:6px solid pink;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  height:100vh;
}
</style>