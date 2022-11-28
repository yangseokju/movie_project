<template>
  <!-- movieDetail이 영화정보 -->
  <div style="height:130vh">
    <div class="wrapper card h-100 col row g-4" :style="{'background-image':`url(${movieDetail.backdrop_path})`}">
      <div class="container p-3 mt-3">
        <div class="container neumorph p-5">
          <div class="detail p-3 neumorph3">
            <div class="row">
              <h2><b>{{ movieDetail.title }}</b></h2>
              <div class="col-12 col-lg-4 align-items-center p-3">
                <img :src="movieDetail.poster_path" alt="" class="img-fluid">
              </div>
              <div class="col-12 col-lg-8 p-3">
                <div class="description mx-3 mt-3">
                <h6 class="my-3"><b>{{ movieDetail.release_date }} 개봉</b></h6>
                <h6 class="my-3"><b>장르 :
                <span v-for="(genre, index) in movieDetail.genre" :key="index">
                  {{ genre.name }}
                </span></b></h6>
                <h6 class="my-3"><b>평점 : {{ movieDetail.vote_avg }}</b></h6>
                <div>
                  <span v-if="movieDetail.overview !==''">
                    {{ movieDetail.overview }}
                  </span>
                  <span v-if="movieDetail.overview ===''">
                    영화소개가 없습니다😢
                  </span>
                </div>
                <!-- 뒤로가기 버튼 -->
              <div>
                <button type="button" class="btn btn-danger mt-5" style="height: 40px; width:200px;" @click="goBack">BACK</button>
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
  import { mapGetters, mapActions } from 'vuex'
  export default {
    name: 'MovieDetailView',
    data() {
      return {
        movie_pk:this.$route.params.movie_pk
      }
    },
    components: {
    },
    computed: {
      ...mapGetters(['movieDetail'])
    },
    methods: {
      ...mapActions(['getMovieDetail',]),
      goBack() {
        this.$router.go(-1)
      }
    },
    updated() {
    },
    created() {
      this.getMovieDetail(this.movie_pk)
    }
  }
  </script>
  
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

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
    background-size: contain;
    background-position: center;
    background-repeat: no-repeat;
  }

  .detail {
    align-content: center;
    width: 70%;
    height: 100%;
    border: 1px solid; 
    padding:30px; 
    background-color: white; 
    color:black;
    margin:0 auto;
    border-radius: 20px;

    font-family: 'Jua', sans-serif;
  }

  </style>