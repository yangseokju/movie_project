import axios from 'axios'
import djangourl from '@/urls/djangourl'


const state = {
    MovieDatas:[],
    movieDetail: [],
    genre_movies: [],
    searchedMovies:[],
}

const getters = {
    movies(state) {
        return state.MovieDatas
    },
    movieDetail(state) {
        return state.movieDetail
    },
    genre_movies(state) {
        return state.genre_movies
    },
    searchedMovies(state) {
        return state.searchedMovies
    },

}

const mutations = {
    GET_MOVIES(state, movieDatas) {
        state.searchedMovies = []
        state.MovieDatas = movieDatas
    },
    GET_MOVIE_DETAIL(state, movieDetail) {
        state.movieDetail = movieDetail
        // state.movieDetailReviews = movieDetail.reviews
        // state.reviews = movieDetail.reviews
    },
    GENRE_MOVIE(state, genre_movies) {
        state.genre_movies = genre_movies
    },
    SET_SEARCHED_MOVIES(state, searchedMovies) {
        state.searchedMovies = searchedMovies
    },

}

const actions = {
    getMovies({ commit }) {
        axios.get(djangourl.URL + djangourl.ROUTES.get_movie_list())
        .then(res => commit('GET_MOVIES', res.data))
        .catch(err => console.error(err))
    },
    getMovieDetail({ commit }, movie_pk) {
        axios.get(djangourl.URL + djangourl.ROUTES.get_movie_detail(movie_pk))
          .then(res => commit('GET_MOVIE_DETAIL', res.data))
          .catch(err => console.error(err))
    },
    genre_movie({commit}, genre_movies) {
        commit('GENRE_MOVIE', genre_movies)
    },
    searchMovies({ getters, commit }, query) {
        const movies = getters.movies
        const searchedMovies = movies.filter(movie => movie.title.includes(query.trim()))
        commit('SET_SEARCHED_MOVIES', searchedMovies)
    },

}

export default {
    state, getters, mutations, actions
}