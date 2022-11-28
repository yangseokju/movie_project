<template>
  <div style="height:130vh">
  <div id="ArticleView">
    <div id="ArticleViewTop">
      <span id="article-view-top-title">{{article.title}}</span>
      <span id="article-view-top-date">작성일: {{createdDate}}ㅤ | ㅤ수정일: {{updatedDate}}</span>
      <router-link :to="{ name: 'profile', params: goToUserPRofile }">
        <b-button id="user-button" variant="light">작성자 : {{article.user.username}}</b-button>  
      </router-link>
    </div>
    <hr>

    <div id="ArticleViewMiddle">
      <p>{{article.content}}</p>
    </div>
    

    <div id="article-view-middle-buttons">
      <b-button id="like-button" v-if="!isAuthor" @click="articleLike(article.pk)">{{isLikedButton}}  {{article.like_users.length}}</b-button>
      
      <router-link v-if="isAuthor" :to="{ name:'ArticleUpdate', params:{articlePk} }">
        <b-button id="article-view-update-button" class="m-3"><b-icon icon="pencil-square"></b-icon></b-button>
      </router-link>

      <b-button v-if="isAuthor" variant="danger" id="article-view-delete-button" type="submit" @click="articleDelete(articlePk)"><b-icon icon="trash"></b-icon></b-button>

      <router-link :to="{ name: 'community' }">
        <b-button id="article-view-back-button" class="m-3"><b-icon icon="list-task"></b-icon></b-button>
        </router-link>
    </div>

    <div id="ArticleViewBottom">
      <article-and-comment-error-list v-if="articleAndCommentError"> </article-and-comment-error-list>
      <comment-list v-for="comment in article.comments" :key="comment.pk" :comment="comment"></comment-list>
      
      <comment-create-form></comment-create-form>
    </div>
  </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import CommentList from '@/components/communities/CommentList.vue'
import CommentCreateForm from '@/components/communities/CommentCreateForm.vue'
import ArticleAndCommentErrorList from '@/components/communities/ArticleAndCommentErrorList.vue'

export default {
  name: 'ArticleView',
  components: {CommentList, CommentCreateForm, ArticleAndCommentErrorList},
  data(){
    return {
      articlePk: this.$route.params.articlePk,
    }
  },
  computed:{
    ...mapGetters(['article', 'isAuthor', 'articleAndCommentError', 'currentUser']),
    goToUserPRofile(){
      return {username: this.article.user.username}
    },
    createdDate(){
      const dateText = this.article.created_at
      const year = dateText.split('T')[0].substring(0,4)
      const month = dateText.split('T')[0].substring(5,7)
      const day = dateText.split('T')[0].substring(8,10)
      const hour = dateText.split('T')[1].substring(0,2)
      const minute = dateText.split('T')[1].substring(3,5)
      const second = dateText.split('T')[1].substring(6,8)
      return `${year}. ${month}. ${day} ${hour}: ${minute}: ${second}`
    },
    updatedDate(){
      const dateText = this.article.updated_at
      const year = dateText.split('T')[0].substring(0,4)
      const month = dateText.split('T')[0].substring(5,7)
      const day = dateText.split('T')[0].substring(8,10)
      const hour = dateText.split('T')[1].substring(0,2)
      const minute = dateText.split('T')[1].substring(3,5)
      const second = dateText.split('T')[1].substring(6,8)
      return `${year}. ${month}. ${day} ${hour}: ${minute}: ${second}`
    },
    isLikedButton(){
      if(this.article.like_users.find(e => e.pk === this.currentUser.pk)){
        return '❤️'
      } else{ 
        return '🤍'
      }
    }
  },
  methods:{
    ...mapActions(['articleGet', 'articleDelete', 'articleLike']),
  },
  created(){
    this.articleGet(this.articlePk)
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');


#ArticleView {
  width: 700px !important;
  display: flex;  
  flex-direction: column;
  justify-content:space-between;
  font-size: 20px;
  color: black;
  font-family: 'Jua', sans-serif;
  
  align-content: center;
  width: 70%;
  height: auto;
  border: 1px solid; 
  padding:30px; 
  background-color: white; 
  color:black;
  margin:0 auto;
  border-radius: 20px;
  font-family: 'Jua', sans-serif;
}

#ArticleViewTop {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

#article-view-top-title{
  font-size:30px;
  font-weight:bold;
}

#article-view-top-date{
  font-size: 15px;
}

#ArticleViewMiddle{
  height: 300px;
  width: 100%;
  padding: 10px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-top: 10px;
  margin-bottom: 10px;
  background-color: white;
}

#like-button{
  background-color:transparent;
  color: black;
}

#article-view-update-button{
  width:50px; height:50px;
  background-color: rgb(20, 20, 207);
}

#article-view-delete-button{
  width:50px; height:50px;
  background-color: rgb(181, 18, 18);
}

#article-view-back-button{
  width:50px; height:50px;
  background-color: #458b22;
}

#article-view-middle-buttons{
  width: 100%;
  margin-top: 10px;
  margin-bottom: 10px;
}

#ArticleViewBottom {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;  
  margin-top: 10px;
  margin-bottom: 10px;
}

#ArticleViewBottom a{
  align-self: flex-end;
}

#CommentList {
  width: 100%;
  text-align:start;
  margin-top: 5px;
  margin-bottom: 5px;  
}
</style>
