<template>
  <div style="height:100vh">
    <div id="communityView" class="container" style="width: 1000px;">
      <h1 id="community-title">커뮤니티</h1>
      
      <router-link :to="{ name:'articleCreate' }">
        <b-button id="create-button" class="m-3">새 글 작성 <b-icon icon="pencil"></b-icon></b-button> 
      </router-link>

      <b-table id="community-table" 
        :per-page="perPage" 
        :total-rows="rows"
        :current-page="currentPage"
        selectable
        hover
        :items="community" 
        :fields="fields"
        @row-clicked="onRowClicked"
        primary-key="pk">
        <template #cell(created_at)="data">
          {{data.item.created_at.substring(0,10)}}
        </template>
      </b-table>
      
      <div id="community-pagination" class="m-3">
        <b-pagination 
          v-model="currentPage"
          :total-rows="rows"
          :per-page="perPage"
          aria-controls="community-table">
        </b-pagination>
      </div>
    </div>
  </div>
</template>

<script>

import {mapGetters, mapActions} from 'vuex'

export default {
  name: 'CommunityView',
  data(){
    return {
      currentPage: 1,
      perPage: 5,
      fields: [
      {key: 'pk',label: '번 호'},
      {key: 'user.username',label: '작 성 자'},
      {key: 'title',label: '제 목'},
      {key: 'created_at', label: '작 성 일'},
      ]
    }
  },
  methods:{
    ...mapActions(['communityGet', 'articleGet']),
    onRowClicked(item){
      this.$router.push({ name: 'article', params: { articlePk: item.pk } })
    }
  },
  computed: {
    ...mapGetters(['community']),
    rows() {
      return this.community.length
    }
  },
  created(){
    this.communityGet()
  }

}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Merriweather&family=Oleo+Script&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

#create-button{
  background-color: #170572;
  float: right;
}

#community-table{
  color: black;

  border-radius: 20px;
  background-color: rgb(177, 200, 236);
  font-family: 'Jua', sans-serif;
}

#community-pagination{
  display: inline-block;
}

#community-title{
  font-family: 'Jua', sans-serif;
  color: black;
}

#communityView{
  align-content: center;
  width: 300px;
  height: auto;
  border: 1px solid; 
  padding:30px; 
  background-color: white; 
  color:black;
  margin:0 auto;
  border-radius: 20px;
  font-family: 'Jua', sans-serif;
}

</style>
