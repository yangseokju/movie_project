<template>
    <div>
        <div class="col">
        <div class="card h-100">
            <img :src="'https://www.themoviedb.org/t/p/w300_and_h450_bestv2'+movie.poster_path" class="card-img-top" alt="...">
            <div class="card-body mb-4" style="width:100%; height:25vh; overflow: hidden;">
                <h5 class="card-title"><b>{{movie.title}}</b></h5>
                <p class="card-text"><b>평점 : {{movie.vote_average}}</b></p>
                <p class="card-text cardpoint" style="">{{movie.overview}}</p>
            </div>
        </div>
        </div>
    </div>
</template>

<script>
export default {
    name:'MovieCard',
    props: {
        'movie':Object,
    }
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
  /* overflow: hidden !important; */
  text-overflow: ellipsis;
  -webkit-line-clamp: 5;
  /* display: -webkit-box;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
  -webkit-line-clamp : 6; */
}
</style>