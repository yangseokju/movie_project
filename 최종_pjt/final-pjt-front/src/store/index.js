import Vue from 'vue'
import Vuex from 'vuex'

import accounts from './modules/accounts'
import communities from './modules/communities'
import movies from '@/store/modules/movies'
import random_movie from '@/store/modules/random_movie'

Vue.use(Vuex)

export default new Vuex.Store({
  modules:{
    accounts,
    communities,
    movies,
    random_movie,
  }

})