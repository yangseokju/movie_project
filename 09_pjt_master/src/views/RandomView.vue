<template>
    <div v-if="movieData">
      <h1 style="color:aqua"><b>{{weather}}한 날씨에 이런 영화 어때요?</b></h1>
      <button type="button" class="btn btn-lg btn-success col-6 mb-3" style="--bs-btn-font-weight:600;" @click="movieApi">Pick</button>
      <div class="card h-100 m-auto" style="width:50%;">
          <img :src="'https://www.themoviedb.org/t/p/w300_and_h450_bestv2'+movieData.poster_path" class="" alt="...">
          <div class="card-body">
            <h5 class="card-title"><b>{{movieData.title}}</b></h5>
          </div>
        </div>
    </div>
  </template>
  
  <script>
    import Axios from 'axios';
    import _ from 'lodash'
    // const API_KEY = '9198ea87f7de9b2dba9436007a2e502b'
    const API_URL = `https://api.themoviedb.org/3/movie/popular?api_key=9198ea87f7de9b2dba9436007a2e502b&language=ko-KR&page=1`
    const WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q=Seoul,kor&APPID=99b93b21a2099a108cc211c6bdbc225e'

    export default {
        name: 'RandomView',
        data(){
          return {
              movieData:null,
              weather:null
          }
        },
        methods: {
          movieApi(){
              Axios.get(API_URL)
              .then((response) => {
                  // overview 있는 영화만 출력
                  const datas = response.data.results.filter((movie)=>{
                      return movie.overview
                  })
                  // console.log(response)
                  const datas2 = _.sample(datas)
                  this.movieData = datas2
              })            
              .catch((error)=>{
                  console.log(error)
              })
          },
          weatherApi() {
            Axios.get(WEATHER_URL)
            .then((response) => {
              // console.log(response)
              this.weather = response.data.weather[0].description
            })
          }
    },
    created(){
      this.weatherApi(),
      this.movieApi()
    },
  }

  </script>
  
  <style>
  
  </style>