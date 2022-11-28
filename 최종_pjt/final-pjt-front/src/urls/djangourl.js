const HOST = 'http://localhost:8000/'
// const MOVIE = 'movies/'
const ACCOUNTS = 'accounts/'
// const COMMUNITY = 'community/'
//기존 django에 맞춰서, 원래는 community
const COMMUNITY = 'community/'

export default {
  URL: 'http://127.0.0.1:8000/',
  ROUTES: {
    get_movie_list() {
      return 'movies/'
    },
    get_movie_detail(movie_pk) {
      return `movies/${movie_pk}`
    },
  },


  admin: {  
    admin:() => HOST + 'admin/'
  },
  accounts:{
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    userProfile: username => HOST + ACCOUNTS + 'profile/' + username,
    // userDelete: username => HOST + ACCOUNTS + 'profile/' + username + '/delete/',
    userFollow: username => HOST + ACCOUNTS + 'profile/' + username + '/follow/',
  },
  communities:{
    community: () => HOST + COMMUNITY,
    article: articlePk => HOST + COMMUNITY + `${articlePk}/`,
    articleLike: articlePk => HOST + COMMUNITY + `${articlePk}/` + 'like/',
    commentCreate: articlePk => HOST + COMMUNITY + `${articlePk}/` + 'comments/',
    commentUpdateDelete: (articlePk, commentPk) => HOST + COMMUNITY + `${articlePk}/comments/${commentPk}/`,
    commentLike: (articlePk, commentPk) => HOST + COMMUNITY + `${articlePk}/${commentPk}/` + 'like/',

  }
}