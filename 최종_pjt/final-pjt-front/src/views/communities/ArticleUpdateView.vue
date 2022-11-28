<template>
  <div style="height:100vh">
  <div id="ArticleUpdateView" >
    <article-and-comment-error-list v-if="articleAndCommentError"> </article-and-comment-error-list>
    <article-form v-if="isArticle" :article="article" action="수정"></article-form>
  </div>
</div>
</template>

<script>
import ArticleForm from '@/components/communities/ArticleForm.vue'
import ArticleAndCommentErrorList from '@/components/communities/ArticleAndCommentErrorList.vue'
import {mapGetters, mapActions} from 'vuex'

export default {
  name:'ArticleUpdateView',
  components: { ArticleForm, ArticleAndCommentErrorList },
  computed:{
    ...mapGetters(['article', 'isArticle', 'articleAndCommentError'])
  },
  methods:{
    ...mapActions(['articleGet'])
  },
  created(){
    this.articleGet(this.$route.params.articlePk)
    console.log('articleupdateviewcreated',this.article.title)
  },
}
</script>

<style scoped>
#ArticleUpdateView {
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
