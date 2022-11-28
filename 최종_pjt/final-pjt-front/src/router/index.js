import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'

import HomeView from '@/views/HomeView.vue'
import MoviesView from '@/views/movies/MovieView.vue'
import MoviesDetail from '@/views/movies/MovieDetailView.vue'
import RandomView from '@/views/movies/RandomView'
import GenreMovie from '@/components/GenreMovie'

import SignupView from '@/views/accounts/SignupView.vue'
import LoginView from '@/views/accounts/LoginView.vue'
import ProfileView from '@/views/accounts/ProfileView.vue'

import CommunityView from '@/views/communities/CommunityView.vue'
import ArticleView from '@/views/communities/ArticleView.vue'
import ArticleCreateView from '@/views/communities/ArticleCreateView.vue'
import ArticleUpdateView from '@/views/communities/ArticleUpdateView.vue'

import NotFound404 from '@/views/NotFound404.vue'

Vue.use(VueRouter)

const routes = [
  //메인 홈페이지
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/movies/:movie_pk',
    name: 'moviesDetail',
    component: MoviesDetail
  },
  {
    path: '/movies',
    name: 'movies',
    component: MoviesView
  },
  {
    path: '/random',
    name: 'RandomView',
    component: RandomView,
    meta: {
      enterClass: "animate__animated animate__zoomIn",
      leaveClass: "animate__animated animate__zoomOut"
    }
  },
  {
    path: '/genre_movies',
    name: 'GenreMovie',
    component: GenreMovie,
    meta: {
      enterClass: "animate__animated animate__zoomIn",
      leaveClass: "animate__animated animate__zoomOut"
    }
  },

  //계정 기능
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView
  },

  //커뮤니티 기능
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/community/create',
    name: 'articleCreate',
    component: ArticleCreateView
  },
  {
    path: '/community/:articlePk',
    name: 'article',
    component: ArticleView
  },
  {
    path: '/community/:articlePk/update',
    name: 'ArticleUpdate',
    component: ArticleUpdateView
  },

  //에러
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  // 이전 페이지에서 발생한 에러메시지 삭제
  store.commit('SET_AUTH_ERROR', null)

  const { isLoggedIn } = store.getters

  const noAuthPages = ['login','signup']
  const noAuthPages2 = ['home','movies','login','signup']

  const isAuthRequired = !noAuthPages.includes(to.name)
  const isAuthRequired2 = !noAuthPages2.includes(to.name)

  if (isAuthRequired2 && !isLoggedIn) {
    // alert('Require Login. Redirecting..')
    next({ name: 'login' })
  } else {
    next()
  }

  if (!isAuthRequired && isLoggedIn) {
    next({ name: 'home'})
  }
})

export default router