import router from '@/router'
import djangourl from '@/urls/djangourl'
import axios from 'axios'

export default {
  state: {
    token: localStorage.getItem('token') || '',
    currentUser: {},
    userProfile: {},
    authError: null,
  },
  getters: {
    isLoggedIn(state) {
      return !!state.token
    },
    currentUser(state) {
      return state.currentUser
    },
    userProfile(state) {
      return state.userProfile
    },
    authError(state) {
      return state.authError
    },
    authHeader(state) {
      return ({Authorization: `Token ${state.token}`})
    }
  },
  mutations: {
    SET_TOKEN(state, token){
      return state.token = token
    },
    SET_CURRENT_USER(state, user) {
      return state.currentUser = user
    },
    SET_USER_PROFILE(state, userProfile) {
      return state.userProfile = userProfile
    },
    SET_USER_PROFILE_FOLLOW(state, userProfile) {
      return state.userProfile = userProfile

    },
    SET_AUTH_ERROR(state, error) {
      return state.authError = error
    }
  },
  actions: {
    setToken({commit}, token){
      commit('SET_TOKEN', token)
      localStorage.setItem('token',token)
    },
    removeToken({commit}){
      commit('SET_TOKEN')
      localStorage.setItem('token','')
    },

    signUp({commit, dispatch, getters}, credentials){
      axios({
        url: djangourl.accounts.signup(),
        method: 'post',
        data: credentials
      })
      .then(res => {
        dispatch('setToken', res.data.key)
        dispatch('getCurrentUser')
        setTimeout(
          function(){
            dispatch('getUserProfile', {username: getters.currentUser.username})
            router.push({name: 'profile', params:{ username: getters.currentUser.username }})
          }, 10
        )
      })
      .catch(err => {
        console.error(err.response.data)
        commit('SET_AUTH_ERROR', err.response.data)
      })
    },

    login({commit, dispatch, getters}, credentials){
      console.log('login에서', credentials)
      axios({
        url: djangourl.accounts.login(),
        method: 'post',
        data: credentials
      })
      .then(res => {
        dispatch('setToken', res.data.key)
        dispatch('getCurrentUser')
        setTimeout(
          function(){
            console.log('로그인 후 currentUser',getters.currentUser)
            dispatch('getUserProfile', {username: getters.currentUser.username})
            router.push({name: 'profile', params:{ username: getters.currentUser.username }})
          }, 10
        )
      })
      .catch(err => {
        console.error(err.response.data)
        commit('SET_AUTH_ERROR', err.response.data)
      })
    },
    logout({getters, dispatch, commit}){
      if(confirm('정말로 로그아웃 하시겠습니까?')){
        axios({
          url: djangourl.accounts.logout(),
          method: 'post',
          headers: getters.authHeader
        })
        .then(() => {
          dispatch('removeToken')
          commit('SET_CURRENT_USER', {})
          alert('성공적으로 로그아웃하셨습니다!')
          router.push({name: 'home'})
        })
        .catch(err => {
          console.error(err.response.data)
        })
      }
    },
    getCurrentUser({commit, getters, dispatch}){
      if (getters.isLoggedIn){
        axios({
          url: djangourl.accounts.currentUserInfo(),
          method: 'get',
          headers: getters.authHeader
        })
        .then(res => {
          commit('SET_CURRENT_USER', res.data)
        })
        .catch(err => {
          if(err.response.status === 401) {
            dispatch('removeToken')
            router.push({ name: 'login' })
          }
        })
      }
    },

    getUserProfile({commit, getters}, {username}){
      axios({
        method: 'get',
        url: djangourl.accounts.userProfile(username),
        headers: getters.authHeader
      })
      .then(res => {
        commit('SET_USER_PROFILE', res.data)
      })
      .catch(err => {
        console.error(err.response)
      })
    },

    userFollow({commit, getters}){
      const username = getters.userProfile.username
      axios({
        method: 'post',
        url: djangourl.accounts.userFollow(username),
        headers: getters.authHeader
      })
      .then(res => {
        commit('SET_USER_PROFILE_FOLLOW', res.data)
        console.log(res.data)
      })
      .catch(err => {
        console.error(err.response)
      })
    },
  },

}
