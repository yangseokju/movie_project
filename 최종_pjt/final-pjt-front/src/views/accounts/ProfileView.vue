<template>
  <div id="main" class="container">
    <div id="Profile-basic" class="mb-5">
      <img id="profileicon" src="../../assets/profile2.png" width="100" height="100" alt="profilelogo" class="m-3">
      <h1 align="center">{{userProfile.username}}</h1>
      <br>
      <h5  id="follow">팔로워 수 : {{followers}} ㅤㅤ 팔로잉 수 : {{followings}}</h5>
      <!-- 내가 아닌 타유저 팔로우 기능 -->
      <b-button variant="primary" v-if="userProfile.username != currentUser.username" @click="userFollow" class="mt-2">
        {{followButton}}
      </b-button>
    </div>
    <hr style="color: black; margin: 0px;">

    <!-- 내가 쓴 게시글 -->
    <div id="Profile-main">
      <div style="background-color: #DBE2EF; text-align: left; font-size: 20px;">ㅤㅤ작성한 게시글 {{ userArticleList.length }} ㅤ|ㅤ 작성한 댓글 {{ userCommentList.length }} </div>
      <hr style="color: black; margin: 0px;">
      <br><br>
      <div id="profile-article">
        <h5 v-if="userProfile.username == currentUser.username" style="float: left;">ㅤ나의 게시글</h5>
        <h5 v-else style="float: left;">ㅤ{{userProfile.username}}님의 게시글</h5>
        <br>
        <template v-if="userArticleList.length===0"><br>
          ㅤ아직 작성한 게시글이 없습니다.
        </template>
        <template v-else> 
          <b-table id="profile-article-table" 
          :per-page="perPage" 
          :total-rows="articleRows"
          :current-page="currentArticlePage"
          :fields="articleField"
          hover
          @row-clicked="articleOnRowClicked"
          primary-key="pk"
          :items="userArticleList"
          style="text-align:center;">
          </b-table>
        </template>
      </div>

      <br>
      
      <br>

      <!-- 내가 쓴 댓글 -->
      <div id="profile-comment">
        <h5 v-if="userProfile.username == currentUser.username" style="float: left;">ㅤ나의 댓글</h5>
        <h5 v-else style="float: left;">ㅤ{{userProfile.username}}님의 댓글</h5>
        <br>
        <template v-if="userCommentList.length===0"><br>
          ㅤ아직 작성한 댓글이 없습니다.
        </template>
        <template v-else> 
          <b-table id="profile-comment-table" 
            :fields="commentFields"
            :per-page="perPage" 
            :total-rows="commentRows"
            :current-page="currentCommentPage"
            hover 
            @row-clicked="commentOnRowClicked"
            primary-key="pk"
            :items="userCommentList">
          </b-table>
        </template>
      </div>
      <br>
    </div>

    <br>
    
    <!-- 내가 추천한 게시글 -->
    <div id="profile-like">
      <h5 v-if="userProfile.username == currentUser.username" style="float: left; color: black;">ㅤ좋아하는 게시글</h5>
      <h5 v-else style="float: left; color: black;">ㅤ{{userProfile.username}}님이 좋아하는 게시글 </h5>
      <br>
      
      <template v-if="userLikeArticleList.length===0"><br>
        ㅤ좋아하는 게시글이 없습니다.
      </template>
      <template v-else> 
        <b-table id="profile-like-table" 
          :fields="articleLikeFields"
          :per-page="perPage"
          hover
          :total-rows="likeArticleRows"
          :current-page="currentLikeArticlePage"
          @row-clicked="articleLikeOnRowClicked"
          :items="userLikeArticleList">
        </b-table>
      </template>
    </div>
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'

export default {
  name: 'ProfileView',
  data(){
    return {
      currentArticlePage: 1,
      currentCommentPage: 1,
      currentLikeArticlePage: 1,
      currentLikeCommentPage: 1,
      perPage: 10,
      articleField: [
        {key: 'pk', thClass: 'd-none', tdClass: 'd-none'},
        {key: 'title',label: '* 게시글 목록 *'},
        {key: 'content', thClass: 'd-none', tdClass: 'd-none'},
      ],
      commentFields: [
        {key: 'pk', thClass: 'd-none', tdClass: 'd-none'},
        {key: 'content', label:'* 댓글 목록 *'},
        {key: 'article', thClass: 'd-none', tdClass: 'd-none'}
      ],
      articleLikeFields: [
        {key: 'pk', thClass: 'd-none', tdClass: 'd-none'},
        {key: 'title', label:'* 좋아요한 게시글 목록 *'},
        {key: 'content', thClass: 'd-none', tdClass: 'd-none'},
      ],
    }
  },
  methods: {
    ...mapActions(['getUserProfile', 'userFollow', 'userDelete']),
    articleOnRowClicked(item){
      this.$router.push({ name: 'article', params: { articlePk: item.pk } })
    },
    commentOnRowClicked(item){
      this.$router.push({ name: 'article', params: { articlePk: item.article } })
    },
    articleLikeOnRowClicked(item){
      this.$router.push({ name: 'article', params: { articlePk: item.pk } })
    },
  },
  computed:{
    ...mapGetters(['userProfile', 'currentUser']),
    followers(){
      return this.userProfile.followers ? this.userProfile.followers.length : 0
    },
    followings(){
      return this.userProfile.followings ? this.userProfile.followings.length : 0
    },
    followButton(){
      if(this.userProfile.followers.find(e => e === this.currentUser.pk)){
        return '팔로우 취소'
      } else {
        return ' 팔로우'
      }
    },

    userArticleList(){
      return this.userProfile.articles
    },
    userCommentList(){
      return this.userProfile.comments
    },
    userLikeArticleList(){
      return this.userProfile.like_articles
    },
    userLikeCommentList(){
      return this.userProfile.like_comments
    },

    articleRows() {
      return this.userArticleList.length
    },
    commentRows(){
      return this.userCommentList.length
    },
    likeArticleRows() {
      return this.userLikeArticleList.length
    },
    likeCommentRows(){
      return this.userLikeCommentList.length
    },
  },
  created(){
    const username = {username: this.$route.params.username} 
    this.getUserProfile(username)
  }

}
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');

#main{
  width:700px;
  height: auto;
  border: 1px solid; 
  padding:30px; 
  background-color: white; 
  color:black;
  margin:0 auto;
  border-radius: 20px;

  font-family: 'Jua', sans-serif;
}

#Profile-basic{
  border: 1px solid; 
  padding:30px; 
  background-color:rgb(177, 200, 236);
  color:black; 
  padding:none;
  border-radius: 10px;
  border-color:white;
}
#Profile-basic, #Profile-main{
  color: black;
}

#profile-article-table, #profile-comment-table, #profile-like-table{
  background-color: rgb(255, 255, 255);
  border-radius: 20px;
  color: black;

}
</style>
