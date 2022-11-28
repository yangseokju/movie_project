import axios from 'axios'
import djangourl from '@/urls/djangourl'
// import _ from 'lodash'

const state = {
    random_movie:[],
}

const getters = {
    random_movies(state) {
        return state.random_movie
    }
}

const mutations = {
    RANDOM_MOVIES(state, random_movie) {
        state.random_movie = random_movie
    }
}

const actions = {
    random_Movies({ commit }, movie_pk) {
        axios.get(djangourl.URL + djangourl.ROUTES.get_movie_detail(movie_pk))
        .then(res => {commit('RANDOM_MOVIES', res.data)})
        .catch(err => console.error(err))
      }
}

export default {
    state, getters, mutations, actions
}