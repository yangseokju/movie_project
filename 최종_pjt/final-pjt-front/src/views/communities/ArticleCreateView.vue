<template>
  <div style="height:100vh">
  <div id="ArticleCreateView" >
    <article-and-comment-error-list v-if="articleAndCommentError"> </article-and-comment-error-list>
    <article-form :article="article" action="작성"></article-form>
  </div>
</div>
</template>

<script>
import ArticleForm from '@/components/communities/ArticleForm.vue'
import ArticleAndCommentErrorList from '@/components/communities/ArticleAndCommentErrorList.vue'
import {mapGetters} from 'vuex'

export default {
  name: 'ArticleCreateView',
  components: { ArticleForm, ArticleAndCommentErrorList },
  data(){
    return {
      article: {
        title: '', 
        content: '',
      }
    }
  },
  computed:{
    ...mapGetters(['articleAndCommentError'])
  }
}
</script>

<style scoped>
#ArticleCreateView {
  width: 700px !important;
  display: flex;
  flex-direction: column;
  justify-content:flex-start;
  width: 70%;
  height: 530px;
  border: 1px solid; 
  padding:30px; 
  background-color: white; 
  color:black;
  margin:0 auto;
  border-radius: 20px;

  font-family: 'Jua', sans-serif;
}


</style>
